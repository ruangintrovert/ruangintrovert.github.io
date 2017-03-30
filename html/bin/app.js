$("body").css("min-height", $(window).height())
$(".markdown").html(marked($("textarea").val()))
tanggalan = new Date
jam = tanggalan.getHours()
if (jam < 5 || jam > 19 && $(window).width() > 590){
    $("body").css("background", "url('bin/rasi bintang.png')")
}