class lyric:
    def __init__(self, _words, _time, _interval, _mode):
        '''
        Interval: -1 means to calculate based on last
        Mode:   0: Lyric with new line
                1: Lyric without new line
                2: ASCII art
                3: Clear lyrics
                4: Start music
                5: Start credits
                9: END
        '''
        self.words = _words
        self.time = _time
        self.interval = _interval
        self.mode = _mode

lyrics = {
'en_US': [
    ##########  Page 1  ##########
    lyric("Forms FORM-29827281-12:",            0,      -1,   0),
    lyric("Test Assessment Report",             200,    -1,   0),
    lyric("\00\00\00\00\00\00\00",              400,    - \
          1,   0),  # Keep flushing the buffer
    lyric("",                                   710,    0,    4),  # Music start
    lyric("This was a triumph.",                730,    2,    0),
    lyric("",                                   930,    0,    5),  # Credits start
    lyric("I'm making a note here:",            1123,   2,    0),
    lyric("HUGE SUCCESS.",                      1347,   1.7,  0),
    lyric("It's hard to overstate",             1627,   -1,   0),
    lyric("my satisfaction.",                   1873,   2.6,  0),
    lyric("Aperture Science",                   2350,   1.8,  0),
    lyric(0,                                    2350,   0,    2),  # ASCII 1
    lyric("We do what we must",                 2733,   1.6,  0),
    lyric("because we can.",                    2910,   1.5,  0),
    lyric("For the good of all of us.",         3237,   -1,   0),
    lyric(1,                                    3500,   0,    2),  # ASCII 2
    lyric("Except the ones who are dead.",      3567,   -1,   0),
    lyric("",                                   3717,   0.05, 0),
    lyric(0,                                    3717,   0,    2),  # ASCII 1
    lyric("But there's no sense crying",        3787,   -1,   0),
    lyric("over every mistake.",                3973,   1.77, 0),
    lyric("You just keep on trying",            4170,   -1,   0),
    lyric("till you run out of cake.",          4370,   -1,   0),
    lyric(2,                                    4500,   0,    2),  # ASCII 3
    lyric("And the Science gets done.",         4570,   -1,   0),
    lyric("And you make a neat gun.",           4767,   -1,   0),
    lyric(0,                                    4903,   0,    2),  # ASCII 1
    lyric("For the people who are",             4973,   -1,   0),
    lyric("still alive.",                       5110,   1.6,  1),

    ##########  Page 2  ##########
    lyric(0,                                    5353,
          0,    3),  # Clear lyrics
    lyric("Forms FORM-55551-5:",                5413,   -1,   0),
    lyric("Personnel File Addendum:",           5477,   1.13, 0),
    lyric("",                                   5650,   0.05, 0),
    lyric("Dear <<Subject Name Here>>,",        5650,   -1,   0),
    lyric("",                                   5900,   -1,   0),
    lyric("I'm not even angry.",                5900,   1.86, 0),
    lyric("I'm being ",                         6320,   -1,   1),
    lyric("so ",                                6413,   -1,   1),
    lyric("sincere right now.",                 6470,   1.9,  0),
    lyric("Even though you broke ",             6827,   -1,   1),
    lyric(3,                                    7020,   0,    2),  # ASCII 4
    lyric("my heart.",                          7090,   -1,   0),
    lyric("And killed me.",                     7170,   1.43, 0),
    lyric(4,                                    7300,   0,    2),  # ASCII 5
    lyric("And tore me to pieces.",             7500,   1.83, 0),
    lyric("And threw every piece ",             7900,   -1,   1),
    lyric("into a fire.",                       8080,   1.8,  0),
    lyric(5,                                    8080,   0,    2),  # ASCII 6
    lyric("As they burned it hurt because",     8430,   -1,   0),
    lyric(6,                                    8690,   0,    2),  # ASCII 7
    lyric("I was so happy for you!",            8760,   1.67, 0),
    lyric("Now these points of data",           8960,   -1,   0),
    lyric("make a beautiful line.",             9167,   -1,   0),
    lyric("And we're out of beta.",             9357,   -1,   0),
    lyric("We're releasing on time.",           9560,   -1,   0),
    lyric(4,                                    9700,   0,    2),  # ASCII 5
    lyric("So I'm GLaD. I got burned.",         9770,   -1,   0),
    lyric(2,                                    9913,   0,    2),  # ASCII 3
    lyric("Think of all the things we learned", 9983,   -1,   0),
    lyric(0,                                    10120,  0,    2),  # ASCII 1
    lyric("for the people who are",             10190,  -1,   0),
    lyric("still alive.",                       10327,  1.8,  0),

    ##########  Page 3  ##########
    lyric(0,                                    10603,
          0,    3),  # Clear lyrics
    lyric("Forms FORM-55551-6:",                10663,  -1,   0),
    lyric("Personnel File Addendum Addendum:",  10710,  1.36, 0),
    lyric("",                                   10710,  0.05, 0),
    lyric("One last thing:",                    10910,  -1,   0),
    lyric("",                                   11130,  0.05, 0),
    lyric("Go ahead and leave ",                11130,  -1,   1),
    lyric("me.",                                11280,  0.5,  0),
    lyric("I think I prefer to stay ",          11507,  -1,   1),
    lyric("inside.",                            11787,  1.13, 0),
    lyric("Maybe you'll find someone else",     12037,  -1,   0),
    lyric("to help you.",                       12390,  1.23, 0),
    lyric("Maybe Black ",                       12737,  -1,   1),
    lyric(7,                                    12787,  0,    2),  # ASCII 8
    lyric("Mesa...",                            12857,  2.7,  0),
    lyric("THAT WAS A JOKE.",                   13137,  1.46, 1),
    lyric(" FAT CHANCE.",                       13387,  1.1,  0),
    lyric("Anyway, ",                           13620,  -1,   1),
    lyric(8,                                    13670,  0,    2),  # ASCII 9
    lyric("this cake is great.",                13740,  -1,   0),
    lyric("It's so delicious and moist.",       13963,  -1,   0),
    lyric(9,                                    14123,  0,    2),  # ASCII 10
    lyric("Look at me still talking",           14193,  -1,   0),
    lyric(1,                                    14320,  0,    2),  # ASCII 2
    lyric("when there's Science to do.",        14390,  -1,  0),
    lyric(0,                                    14527,  0,    2),  # ASCII 1
    lyric("When I look out there,",             14597,  -1,   0),
    lyric("it makes me GLaD I'm not you.",      14767,  -1,   0),
    lyric(2,                                    14913,  0,    2),  # ASCII 3
    lyric("I've experiments to run.",           14983,  -1,   0),
    lyric(4,                                    15120,  0,    2),  # ASCII 5
    lyric("There is research to be done.",      15190,  -1,   0),
    lyric(0,                                    15320,  0,    2),  # ASCII 1
    lyric("On the people who are",              15390,  -1,   0),
    lyric("still alive",                        15553,  2.0,  1),

    ##########  Page 4  ##########
    lyric(0,                                    15697,
          0,    3),  # Clear lyrics
    lyric("",                                   15757,  0.05, 0),
    lyric("",                                   15757,  0.05, 0),
    lyric("",                                   15757,  0.05, 0),
    lyric("PS: And believe me I am",            15757,  -1,   0),
    lyric("still alive.",                       15960,  1.13, 0),
    lyric("PPS: I'm doing Science and I'm",     16150,  -1,   0),
    lyric("still alive.",                       16363,  1.13, 0),
    lyric("PPPS: I feel FANTASTIC and I'm",     16550,  -1,   0),
    lyric("still alive.",                       16760,  -1,   0),
    lyric("",                                   16860,  -1,   0),
    lyric("FINAL THOUGHT:",                     16860,  -1,   0),
    lyric("While you're dying I'll be",         16993,  -1,   0),
    lyric("still alive.",                       17157,  -1,   0),
    lyric("",                                   17277,  -1,   0),
    lyric("FINAL THOUGHT PS:",                  17277,  -1,   0),
    lyric("And when you're dead I will be",     17367,  -1,   0),
    lyric("still alive.",                       17550,  1.13, 0),
    lyric("",                                   17550,  -1,   0),
    lyric("",                                   17550,  0.05, 0),
    lyric("STILL ALIVE",                        17760,  1.13, 0),
    lyric(0,                                    17900,
          0,    3),  # Clear lyrics
    lyric(0,                                    18500,
          0,    3),  # Clear lyrics
    lyric("ENDENDENDENDENDENDENDEND",           18500,  0.05, 9)
],

'zh_CN': [
    ##########  Page 1  ##########
    lyric("Forms FORM-29827281-12:",            0,      -1,   0),
    lyric("Test Assessment Report",             200,    -1,   0),
    lyric("\00\00\00\00\00\00\00",              400,    - \
          1,   0),  # Keep flushing the buffer
    lyric("",                                   710,    0,    4),  # Music start
    lyric("这是一次伟大的胜利。",                730,    2,    0),
    lyric("",                                   930,    0,    5),  # Credits start
    lyric("我要在这儿做点记录：",            1123,   2,    0),
    lyric("心花怒放。",                      1347,   1.7,  0),
    lyric("我此刻的喜悦之情",             1627,   -1,   0),
    lyric("莫可名状。",                   1873,   2.6,  0),
    lyric("穿梭之力量。",                   2350,   1.8,  0),
    lyric(0,                                    2350,   0,    2),  # ASCII 1
    lyric("我们竭尽全力",                 2733,   1.6,  0),
    lyric("只因 心的方向。",                    2910,   1.5,  0),
    lyric("为了所有 活着的人，",         3237,   -1,   0),
    lyric(1,                                    3500,   0,    2),  # ASCII 2
    lyric("逝者已往。",      3567,   -1,   0),
    lyric("",                                   3717,   0.05, 0),
    lyric(0,                                    3717,   0,    2),  # ASCII 1
    lyric("不必为过去每一次",        3787,   -1,   0),
    lyric("失败而沮丧。",                3973,   1.77, 0),
    lyric("只要你勇于尝试，",            4170,   -1,   0),
    lyric("永不 退让。",          4370,   -1,   0),
    lyric(2,                                    4500,   0,    2),  # ASCII 3
    lyric("力量自然从天而降。",         4570,   -1,   0),
    lyric("你将拥有时空操纵之枪。",           4767,   -1,   0),
    lyric(0,                                    4903,   0,    2),  # ASCII 1
    lyric("为了所有活着的",             4973,   -1,   0),
    lyric("人啊。",                       5110,   1.6,  1),

    ##########  Page 2  ##########
    lyric(0,                                    5353,
          0,    3),  # Clear lyrics
    lyric("Forms FORM-55551-5:",                5413,   -1,   0),
    lyric("Personnel File Addendum:",           5477,   1.13, 0),
    lyric("",                                   5650,   0.05, 0),
    lyric("Dear <<Subject Name Here>>,",        5650,   -1,   0),
    lyric("",                                   5900,   -1,   0),
    lyric("让憎恨随风。",                5900,   1.86, 0),
    lyric("我 ",                         6320,   -1,   1),
    lyric("心境",                                6413,   -1,   1),
    lyric(" 明澄 。",                 6470,   1.9,  0),
    lyric("即使 揉碎 我的 ",             6827,   -1,   1),
    lyric(3,                                    7020,   0,    2),  # ASCII 4
    lyric("心，让",                          7090,   -1,   0),
    lyric("我 不 得生。",                     7170,   1.43, 0),
    lyric(4,                                    7300,   0,    2),  # ASCII 5
    lyric("将我碾为灰尘。",             7500,   1.83, 0),
    lyric("抑或将我 ",             7900,   -1,   1),
    lyric("推入 火炕。",                       8080,   1.8,  0),
    lyric(5,                                    8080,   0,    2),  # ASCII 6
    lyric("我燃烧之时，  略为伤神，",     8430,   -1,   0),
    lyric(6,                                    8690,   0,    2),  # ASCII 7
    lyric("因为我曾是为你喝彩的人。",            8760,   1.67, 0),
    lyric("因我的星光火点，",          8960,   -1,   0),
    lyric("为你打开智慧之门。",             9167,   -1,   0),
    lyric("我凤凰涅盘、",             9357,   -1,   0),
    lyric("浴火重生。",           9560,   -1,   0),
    lyric(4,                                    9700,   0,    2),  # ASCII 5
    lyric("所以我不惧烈火焚身。",          9770,   -1,   0),
    lyric(2,                                    9913,   0,    2),  # ASCII 3
    lyric("我们学会倔强和坚忍。", 9983,   -1,   0),
    lyric(0,                                    10120,  0,    2),  # ASCII 1
    lyric("为了所有",             10190,  -1,   0),
    lyric("活着的 人啊。",                       10327,  1.8,  0),

    ##########  Page 3  ##########
    lyric(0,                                    10603,
          0,    3),  # Clear lyrics
    lyric("Forms FORM-55551-6:",                10663,  -1,   0),
    lyric("Personnel File Addendum Addendum:",  10710,  1.36, 0),
    lyric("",                                   10710,  0.05, 0),
    lyric("One last thing:",                    10910,  -1,   0),
    lyric("",                                   11130,  0.05, 0),
    lyric("走你的路 ",                11130,  -1,   1),
    lyric("莫回头。",                                11280,  0.5,  0),
    lyric("我愿意 一直 在 ",        11507,  -1,   1),
    lyric("你的身后。",                            11787,  1.13, 0),
    lyric("可能有一天你会",     12037,  -1,   0),
    lyric("找到帮助你的新朋友。",                       12390,  1.23, 0),
    lyric("是黑山 的 ",                       12737,  -1,   1),
    lyric(7,                                    12787,  0,    2),  # ASCII 8
    lyric("战友？...",                            12857,  2.7,  0),
    lyric("别做梦啦， ",                   13137,  1.46, 1),
    lyric("哈哈， 机会没有。",                       13387,  1.1,  0),
    lyric("虽然你还有",                           13620,  -1,   1),
    lyric(8,                                    13670,  0,    2),  # ASCII 9
    lyric("很长的路要走。",                13740,  -1,   0),
    lyric("但它汗水相融，幸福相守。",       13963,  -1,   0),
    lyric(9,                                    14123,  0,    2),  # ASCII 10
    lyric("就像我一边聊天，",           14193,  -1,   0),
    lyric(1,                                    14320,  0,    2),  # ASCII 2
    lyric("一边还可以做研究。",        14390,  -1,  0),
    lyric(0,                                    14527,  0,    2),  # ASCII 1
    lyric("眺望前路，",             14597,  -1,   0),
    lyric("我窃喜于不必面对你那些艰难险阻。",      14767,  -1,   0),
    lyric(2,                                    14913,  0,    2),  # ASCII 3
    lyric("我还有实验要做。",           14983,  -1,   0),
    lyric(4,                                    15120,  0,    2),  # ASCII 5
    lyric("我还有报告要补。",      15190,  -1,   0),
    lyric(0,                                    15320,  0,    2),  # ASCII 1
    lyric("为所有",              15390,  -1,   0),
    lyric("活着 的人。",                        15553,  2.0,  1),

    ##########  Page 4  ##########
    lyric(0,                                    15697,
          0,    3),  # Clear lyrics
    lyric("",                                   15757,  0.05, 0),
    lyric("",                                   15757,  0.05, 0),
    lyric("",                                   15757,  0.05, 0),
    lyric("PS: 相信我，",            15757,  -1,   0),
    lyric("我还活着。",                       15960,  1.13, 0),
    lyric("PPS: 我正在做研究，",     16150,  -1,   0),
    lyric("所以我还活着。",                       16363,  1.13, 0),
    lyric("PPPS: 我异想天开，",     16550,  -1,   0),
    lyric("所以我要活着。",                       16760,  -1,   0),
    lyric("",                                   16860,  -1,   0),
    lyric("FINAL THOUGHT:",                      16860,  -1,   0),
    lyric("你垂死之刻，",         16993,  -1,   0),
    lyric("我仍会活着。",                       17157,  -1,   0),
    lyric("",                                   17277,  -1,   0),
    lyric("FINAL THOUGHT PS:",                   17277,  -1,   0),
    lyric("你作古之时，",     17367,  -1,   0),
    lyric("我还会活着。",                       17550,  1.13, 0),
    lyric("",                                   17550,  -1,   0),
    lyric("",                                   17550,  0.05, 0),
    lyric("还活着。",                        17760,  1.13, 0),
    lyric(0,                                    17900,
          0,    3),  # Clear lyrics
    lyric(0,                                    18500,
          0,    3),  # Clear lyrics
    lyric("ENDENDENDENDENDENDENDEND",           18500,  0.05, 9)
]
}