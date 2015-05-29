Title: Automatically tracking my thesis progress
Date: 2014-10-03
Slug: automated-thesis-tracking

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="https://www.google.com/jsapi"></script>

<script>

  // onload callback
  function drawChart() {

    var public_key = 'zDaZOadL0XUKgVp5ojgV';

    // JSONP request
    var jsonData = $.ajax({
      url: 'https://data.sparkfun.com/output/' + public_key + '.json',
      data: {page: 1},
      dataType: 'jsonp',
    }).done(function (results) {

      var data = new google.visualization.DataTable();

      data.addColumn('datetime', 'Time');
      data.addColumn('number', 'wordcount');

      $.each(results, function (i, row) {
        data.addRow([
          (new Date(row.timestamp)),
          parseInt(row.wordcount)
        ]);
      });

      var chart = new google.visualization.LineChart($('#chart').get(0));

      chart.draw(data, {
         title: 'Number of words written for my thesis',
            legend: {position: 'none'},
            pointSize: 4
      });

    });

  }

  // load chart lib
  google.load('visualization', '1', {
    packages: ['corechart']
  });

  // call drawChart once google charts is loaded
  google.setOnLoadCallback(drawChart);

</script>

<div id="chart" style="width: 100%;"></div>

In my ongoing quest to procrastinate writing my [thesis](http://www.github.com/samvrlewis/thesis/) by working on marginally related work so that I still feel vaguely productive, I implemented a simple system to automatically keep track of how many words I've written in my thesis report.  

Conveniently, I'm using LaTeX to write the thesis report. This allowed me to use the cool [texcount](http://app.uio.no/ifi/texcount/) script (included in most TeX distributions) to count the number of words in each of the .tex files in my thesis. The good thing about this script is it won't count the LaTeX markup towards my total word count. 

Needing somewhere to store the word count, and because I've been looking for an excuse to use it, I used SparkFun's [phant](https://data.sparkfun.com/) to create a quick and dirty data stream. The great thing about phant is once you've created the data stream, all that's needed to submit data to it is a single HTTP GET request which is doable in a single line of python. If you're that way inclined, you can see my data stream [here](https://data.sparkfun.com/streams/zDaZOadL0XUKgVp5ojgV).

Because I'm using git as version control, all that was then needed to tie everything together was a [quick python script](https://gist.github.com/samvrlewis/8a1522084bc99eda7651) for the pre-commit git hook to count the words in each of my different sections, add them together and submit the total to my data stream on phant. This runs whenever I commit to git -- so whenever I've actually written something useful. Easy! 

It was then simple to hook into the data stream with google charts. A chart with my progress is shown above, will be interesting to see how the line behaves (I'm expecting an exponential rise closer to the due date!). 