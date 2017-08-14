from lxml import etree
def getData(file):
    uncompilerversion = "0.0.0.3"
    temp = open(file,"r")
    xml = temp.read()
    temp.close()

    xmlt=""
    inCom=False
    for loop in range(len(xml)):
        if inCom == False:
            if xml[loop] == "<" and xml[loop+1] == "!" and xml[loop+2] == "-" and xml[loop+3] == "-":
                inCom = True
        else:
            if xml[loop-1] == ">" and xml[loop-2] == "-" and xml[loop-3] == "-":
                inCom = False
        
        if not inCom:
            xmlt = xmlt + xml[loop]


    root = etree.fromstring(xmlt)

    main = root[0]
    leveldata = { "version" : root.get("gameVersion"),
                  "region" : root.get("gameRegion")}

    scriptPack = []
    for scriptset in root:
        print(scriptset.tag)
        if scriptset.tag == "LSDTable":
            LSDdata = []
            for ref in scriptset:
                LSDdata.append(ref.get("name"))
            print(LSDdata)

        elif scriptset.tag == "ScriptSet":
            name = scriptset.get("name")
            #TODO : triggerTable
            #TODO : position marker
            #TODO : Layer
            script = scriptset[1]
            scriptName = script.get("name")
            code = script[0]
            fonc = []
            for function in code:
                print("--- function ---")
                funcid = function.get("_id")
                funcl = []
                for command in function:
                    tag = command.tag
                    if tag == "sound_Stop":
                        funcl.append({"commande" : "soundStop"})
                    elif tag == "back2_SetMode":
                        obj = {"commande" : "back2SetMode",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "back2_SetGround":
                        obj = {"commande" : "back2SetGround",
                               "levelid" : command.get("levelid")}
                        funcl.append(obj)
                    elif tag == "back_SetGround":
                        obj = {"commande" : "backSetGround",
                               "levelid" : command.get("levelid")}
                        funcl.append(obj)
                    elif tag == "supervision_StationCommon":
                        obj = {"commande" : "supervisionStationCommon",
                               "stationid" : command.get("stationid")}
                        funcl.append(obj)
                    elif tag == "supervision_Acting":
                        obj = {"commande" : "supervisionActing",
                               "layerid" : command.get("layerid")}
                        funcl.append(obj)
                    elif tag == "performer":
                        obj = {"commande" : "performer",
                               "performerid" : command.get("performerid"),
                               "in" : "TODO"}#TODO : in
                        funcl.append(obj)
                    elif tag == "bgm_PlayFadeIn":
                        obj = {"commande" : "bgmPlayFadeIn",
                               "bgm" : command.get("bgm"),
                               "duration" : command.get("duration"),
                               "vol" : command.get("vol")}
                        funcl.append(obj)
                    elif tag == "screen2_FadeIn":
                        obj = {"commande" : "screen2FadeIn",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "screen_FadeIn":
                        obj = {"commande" : "screenFadeIn",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "Wait":
                        obj = {"commande" : "wait",
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "message_SetFace":
                        obj = {"commande" : "messageSetFace",
                               "actorid" : command.get("actorid"),
                               "face" : command.get("face"),
                               "facemode" : command.get("facemode")}
                        funcl.append(obj)
                    elif tag == "message_SwitchTalk":
                        caseText = []
                        defaultText = None
                        for case in command:
                            caset = []
                            for lang in case:
                                caset.append([lang.get("language"),lang.text])
                            if case.tag == "CaseText":
                                caseText.append({"type" : case.keys()[0],
                                                 "value" : case.get(case.keys()[0]),
                                                 "text" : caset})
                            elif case.tag == "DefaultText":
                                defaultText = caset
                            else:
                                print("erreur non bloquante : type de condition de texte non définie.")
                        obj = {"commande" : "messageSwitchTalk",
                               "svar" : command.get("svar"),
                               "case" : caseText,
                               "default" : defaultText}
                        funcl.append(obj)
                    elif tag == "CallCommon":
                        obj = {"commande" : "callCommon",
                               "croutineid" : command.get("croutineid")}
                        funcl.append(obj)
                    elif tag == "lives":
                        obj = {"commande" : "lives",
                               "actorid" : command.get("actorid"),
                               "in" : "TODO"}#TODO : in
                        funcl.append(obj)
                    elif tag == "WaitExecuteLives":
                        obj = {"commande" : "waitExecuteLives",
                               "actorid" : command.get("actorid")}
                        funcl.append(obj)
                    elif tag == "SwitchSector":
                        obj = {"commande" : "switchSector",
                               "in" : "TODO"}#TODO : in
                        funcl.append(obj)
                    elif tag == "End":
                        obj = {"commande" : "end"}
                        funcl.append(obj)
                    elif tag == "message_Talk":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "messageTalk",
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "message_Close":
                        obj = {"commande" : "messageClose"}
                        funcl.append(obj)
                    elif tag == "screen_FadeOut":
                        obj = {"commande" : "screenFadeOut",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "message_SetActor":
                        obj = {"commande" : "messageSetActor",
                               "actorid" : command.get("actorid")}
                        funcl.append(obj)
                    elif tag == "object":
                        obj = {"commande" : "object",
                               "objectid" : command.get("objectid"),
                               "in" : "TODO"}#TODO : in
                        funcl.append(obj)
                    elif tag == "se_Play":
                        obj = {"commande" : "sePlay",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "screen2_FadeOut":
                        obj = {"commande" : "screen2FadeOut",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "bgm_FadeOut":
                        obj = {"commande" : "bgmFadeOut",
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "WaitBgm":
                        obj = {"commande" : "waitBgm",
                               "bgm" : command.get("bgm")}
                        funcl.append(obj)
                    elif tag == "WaitSe":
                        obj = {"commande" : "waitSe",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "camera_SetEffect":
                        obj = {"commande" : "cameraSetEffect",
                                "param" : command.get("param"),
                                "param_1" : command.get("param_1"),
                                "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "WaitExecuteObject":
                        obj = {"commande" : "waitExecuteObject",
                               "objectid" : command.get("objectid")}
                        funcl.append(obj)
                    elif tag == "se_Stop":
                        obj = {"commande" : "seStop",
                               "param" : command.get("param")}
                        funcl.append(obj)
                    elif tag == "message_EmptyActor":
                        obj = {"commande" : "messageEmptyActor"}
                        funcl.append(obj)
                    elif tag == "WaitExecutePerformer":
                        obj = {"commande" : "waitExecutePerformer",
                               "performerid" : command.get("performerid")}
                        funcl.append(obj)
                    elif tag == "message_SwitchMonologue":
                        caseText = []
                        defaultText = None
                        for case in command:
                            caset = []
                            for lang in case:
                                caset.append([lang.get("language"),lang.text])
                            if case.tag == "CaseText":
                                caseText.append({"type" : case.keys()[0],
                                                 "value" : case.get(case.keys()[0]),
                                                 "text" : caset})
                            elif case.tag == "DefaultText":
                                defaultText = caset
                            else:
                                print("erreur non bloquante : type de condition de texte non définie.")
                        obj = {"commande" : "messageSwitchMonologue",
                               "svar" : command.get("svar"),
                               "case" : caseText,
                               "default" : defaultText}
                        funcl.append(obj)
                    elif tag == "message_ResetActor":
                        obj = {"commande" : "messageResetActor"}
                        funcl.append(obj)
                    elif tag == "flag_SetScenario":
                        obj = {"commande" : "flagSetScenario",
                               "svar" : command.get("svar"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "flag_SetDungeonMode":
                        obj = {"commande" : "flagSetDungeonMode",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1")}
                        funcl.append(obj)
                    elif tag == "back_SetBanner2":
                        caset = []
                        for lang in command:
                            caset.append([lang.get("language"),lang.text])
                        obj = {"commande" : "backSetBanner2",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "x" : command.get("x"),
                               "y" : command.get("y"),
                               "param_4" : command.get("param_4"),
                               "text" : caset}
                        funcl.append(obj)
                    elif tag == "screen_FlushIn":
                        obj = {"commande" : "screenFlushIn",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "screen2_FlushIn":
                        obj = {"commande" : "screen2FlushIn",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "screen_FlushOut":
                        obj = {"commande" : "screenFlushOut",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "screen2_FlushOut":
                        obj = {"commande" : "screen2FlushOut",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3"),
                               "param_4" : command.get("param_4"),
                               "param_5" : command.get("param_5")}
                        funcl.append(obj)
                    elif tag == "camera2_SetPositionMark":
                        obj = {"commande" : "camera2SetPositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "camera_SetPositionMark":
                        obj = {"commande" : "cameraSetPositionMark",
                               "param" : command.get("param"),
                               "param_1" : command.get("param_1"),
                               "param_2" : command.get("param_2"),
                               "param_3" : command.get("param_3")}
                        funcl.append(obj)
                    elif tag == "supervision_RemoveActing":
                        obj = {"commande" : "supervisionRemoveActing",
                               "layerid" : command.get("layerid")}
                        funcl.append(obj)
                    elif tag == "message_SetFaceOnly":
                        obj = {"commande" : "messageSetFaceOnly",
                               "actorid" : command.get("actorid"),
                               "face" : command.get("face"),
                               "param_2" : command.get("param_2")}
                        funcl.append(obj)
                    elif tag == "WaitScreenFadeAll":
                        obj = {"commande" : "waitScreenFadeAll"}
                        funcl.append(obj)
                    elif tag == "WaitScreenFade":
                        obj = {"commande" : "waitScreenFade"}
                        funcl.append(obj)
                    elif tag == "SetAnimation":
                        obj = {"commande" : "setAnimation",
                               "animid" : command.get("animid")}
                        funcl.append(obj)
                    elif tag == "screen_FadeOutAll":
                        obj = {"commande" : "screenFadeOutAll",
                               "bool" : command.get("bool"),
                               "duration" : command.get("duration")}
                        funcl.append(obj)
                    elif tag == "Label":
                        obj = {"commande" : "label",
                               "id" : command.get("id")}
                        funcl.append(obj)
                    elif tag == "JumpCommon":
                        obj = {"commande" : "jumpCommon",
                               "croutineid" : command.get("croutineid")}
                        funcl.append(obj)
                    elif tag == "debug_Print":
                        obj = {"commande" : "debugPrint",
                               "constref" : command.get("constref")}
                        funcl.append(obj)
                    elif tag == "Jump":
                        obj = {"commande" : "jump",
                                "tolabel" : command.get("tolabel")}
                        funcl.append(obj)
                    elif tag == "Switch":
                        obj = {"commande" : "switch",
                               "svar" : command.get("svar")}
                        funcl.append(obj)
                        #print(obj)
                    else:
                        print("tag inconnu : " + tag)
                fonc.append({"funcl": funcl,
                             "id" : funcid})
            scriptPack.append({"fonction" : fonc,
                               "name" : name})
        
    rendu = {"game" : leveldata,
             "LSDTable" : LSDdata,
             "script" : scriptPack,
             "version" : uncompilerversion}
    
    return rendu
if __name__ == "__main__":
    print(getData("export/scripts/G01P01B.xml"))
