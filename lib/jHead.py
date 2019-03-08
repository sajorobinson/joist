import string, sys, os, time

today = time.strftime("%A %B %d %Y at %H:%M:%S %Z")

jHead = """<!DOCTYPE html>
<!--[if lte IE 6]><html class="preIE7 preIE8 preIE9"><![endif]-->
<!--[if IE 7]><html class="preIE8 preIE9"><![endif]-->
<!--[if IE 8]><html class="preIE9"><![endif]-->
<!--[if gte IE 9]><!--><html><!--<![endif]-->
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>title</title>
    <meta name="author" content="name">
    <meta name="description" content="description here">
    <meta name="keywords" content="keywords,here">
    <link rel="stylesheet" href="css/style.css" type="text/css">
    <link rel="stylesheet" href="css/customStyle.css" type="text/css">
    <link rel="stylesheet" href="css/navStyle.css" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto:400,700" rel="stylesheet">
</head>
<body>
"""

jBodyEnd = """<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
$('a[href^="#"]').on('click', function(event) {
    var target = $(this.getAttribute('href'));
    if( target.length ) {
        event.preventDefault();
        $('html, body').stop().animate({
            scrollTop: target.offset().top
        }, );
    }
});
</script>
</body>
"""

timeStamp = "\n<!-- CREATED ON " + today.upper() + ". -->\n"

jHtmlEnd = """
</html>
"""
