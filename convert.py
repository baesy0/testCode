r = nuke.nodes.Read(file="/project/circle/in/aces/exr/A005C021_150831_R0D0/A005C021_150831_R0D0.%06d.exr")
w = nuke.nodes.Write(file="/project/circle/in/aces/exr/A005C021_150831_R0D0/A005C021_150831_R0D0.%06d.jpg")
nuke.execute("Write1",156880,156883)
quit()
