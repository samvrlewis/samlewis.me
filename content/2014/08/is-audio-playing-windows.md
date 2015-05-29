Title: Using C# to check if audio is playing in Windows
Date: 2014-08-05
Slug: is-audio-playing-windows

Using the [CSCore](http://cscore.codeplex.com/) library (easily installed in Visual Studio with Install-Package CSCore) I was able to quickly knock up a prototype that let me check if audio was currently being played on my system.

The code below is heavily inspired by audio meter code in the EndPointTests file for CSCore.
	
	using CSCore.CoreAudioAPI;
	using System;

	namespace AudioPlayingTest
	{
	    class AudioPlayChecker
	    {
	        // Gets the default device for the system
	        public static MMDevice GetDefaultRenderDevice()
	        {
	            using (var enumerator = new MMDeviceEnumerator())
	            {
	                return enumerator.GetDefaultAudioEndpoint(DataFlow.Render, Role.Console);
	            }
	        }

	        // Checks if audio is playing on a certain device
	        public static bool IsAudioPlaying(MMDevice device)
	        {
	            using (var meter = AudioMeterInformation.FromDevice(device))
	            {
	                return meter.PeakValue > 0;
	            }
	        }

	        static void Main(string[] args)
	        {
	            Console.WriteLine(IsAudioPlaying(GetDefaultRenderDevice()));
	            Console.ReadLine(); //Just so the console window doesn't close
	        }
	    }
	}

The code is hopefully self explanatory but basically gets the default system audio device, then uses the peak value from a audio meter to determine whether audio is playing.