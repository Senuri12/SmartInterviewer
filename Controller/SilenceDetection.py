
import shutil
import os
from BackEnd.Controller import ConnectionToNeo4j, vari, AudioRecorder


def silence_detect1(QNumber):

    #Passing parameters
    sessionNumber = vari.sessionId
    userId = vari.userId


    outputFile = AudioRecorder.passedParaName


    from pydub import AudioSegment, silence
    path = 'D:/New Research/SmartInterviewer-Code/BackEnd/Database/Audio/'+outputFile
    print(path)
    # os.chdir(path)
    # files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    # oldest = files[0]
    # print(oldest)
    # path1 = path + '/' + oldest
    # print(path1)
    myaudio = AudioSegment.from_wav(path)  # 'audio/output14.wav'

    silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=-50)
    # start and the end point of silence and display number of silent part in brackets
    # convert to sec
    silence = [((start / 1000), (stop / 1000)) for start, stop in silence]
    # Start and end points of silence parts in milliseconds
    print(silence)
    # Gap between start and the end point of the each silent part of the audio
    silence_gap = [(((stop) - (start)) / 1000) for start, stop in silence]
    # Silence gaps display in list
    print(silence_gap)
    # identify silence parts with more than 5 seconds
    silence_gap2 = sorted(i for i in silence_gap if i >= 0.005)
    print(silence_gap2)

    silence_gap_list = [i * 1000 for i in silence_gap2]
    # silence gaps with three decimal places
    myFormattedList2 = ['%.3f' % elem for elem in silence_gap_list]
    print(myFormattedList2)
    # Number of silence gaps with morethan 5 milliseconds
    print(len(myFormattedList2))

    silenceCount=len(myFormattedList2)
    if silenceCount < 1:
        voiceMrks = 25
        print("voiceMrks", voiceMrks)
    elif silenceCount < 2:
        voiceMrks = 22.5
        print("voiceMrks", voiceMrks)
    elif silenceCount < 3:
        voiceMrks = 20
        print("voiceMrks", voiceMrks)
    elif silenceCount < 4:
        voiceMrks = 17.5
        print("voiceMrks", voiceMrks)
    elif silenceCount < 5:
        voiceMrks = 15
        print("voiceMrks", voiceMrks)
    elif silenceCount < 6:
        voiceMrks = 12.5
        print("voiceMrks", voiceMrks)
    elif silenceCount < 7:
        voiceMrks = 10
        print("voiceMrks", voiceMrks)
    elif silenceCount < 8:
        voiceMrks = 7.5
        print("voiceMrks", voiceMrks)
    elif silenceCount < 9:
        voiceMrks = 5
        print("voiceMrks", voiceMrks)
    elif silenceCount < 10:
        voiceMrks = 2.5
        print("voiceMrks", voiceMrks)
    else:
        voiceMrks = 0
        print("voiceMrks", voiceMrks)

#After detecting the silence part of the audio clip it willmove to another folder vikum shold get the audio clip from that new folder.
    #path2 = 'D:/New Research/SmartInterviewer-Code/BackEnd/Database/movedAudio'
    #shutil.move(path1, path2)

    #passed from sarindi



    #------------------------------------------------------------
    string = "voiceq"
    questionNumber = QNumber
    questionOutput = string + str(questionNumber)
    print(questionOutput)
    print(type(questionOutput))

    #----------------------------------------------------
    qnumber = questionOutput
    voiceMark = str(voiceMrks)

    ConnectionToNeo4j.getQuestionNumberToSave(userId,sessionNumber,qnumber)




    ConnectionToNeo4j.saveVoiceMarks(userId,sessionNumber,qnumber, voiceMark)

    print(ConnectionToNeo4j.saveVoiceMarks(userId,sessionNumber,qnumber, voiceMark))


