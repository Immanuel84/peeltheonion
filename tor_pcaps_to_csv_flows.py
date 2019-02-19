# author: EManuele/Immanuel

import util
import os

if __name__ == '__main__':
    # How to use
    # basepath: path to folder that contains other folders with .pcap
    # Ex: captures --|
    #                | youtube -- |
    #                             | youtube_1.pcap
    #                             | youtube_2.pcap
    #
    #                | spotify -- |
    #                             |  spotify_1.pcap
    basepath =  "captures/"
    # output_folder: Self-explicative..
    output_folder = "output/"
    # Each entry is a list [ app, category] where app is also the name of the folder that contains capture
    folders_category = [["torbrowser_alpha", "web_and_social"], ["facebook", "web_and_social"], \
                        ["skype", "voip"], ["youtube", "streaming"], ["spotify", "streaming"], \
                        ["dailymotion", "streaming"], ["twitch", "streaming"], \
                        ["instagram", "web_and_social"], \
                        ["replaio_radio", "streaming"], ["utorrent", "filesharing"]]

    # List of Timeouts to use to compute flows
    timeouts = [10, 15]
    # List of activity timeout to use to ocompute flows (how many sec. before flow is considered idle)
    activity_timeouts = [2, 5]
    for timeout in timeouts:
        for activitytimeout in activity_timeouts:
            for folder in folders_category:
                for file in os.listdir(basepath+folder[0]):
                    if file.endswith(".pcap"):
                        print("Current Folder: %s Current File: %s Current Timeout: %d Activity Timeout: %d" % (basepath+folder[0], file, timeout, activitytimeout))
                        util.ProcessPcapTor(basepath+folder[0]+"/"+file,  output_folder=output_folder, \
                                            label=folder[0], category=folder[1], \
                                            Timeout=timeout, ActivityTimeout=activitytimeout, \
                                            TorPickle="/Users/emanuele/Desktop/University/master_thesis/code/rewritten_public/testing/testvenv/entry_nodes")
