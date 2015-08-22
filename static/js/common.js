function drawNavbar() {
    var $divNav = $('div#nav-bar');
    $('<nav class="navbar navbar-default"></nav>').appendTo($divNav);
    var $con = $('<div class="container-fluid"></div>')
        .append('<div class="navbar-header"></div>')
        .append('<div class="collapse navbar-collapse" id="toolbar"></div>')
        .appendTo($divNav.find('nav'));
    $('<button class="navbar-toggle collapsed"></button>')
        .attr('data-toggle', 'collapse')
        .attr('data-target', '#toolbar')
        .attr('aria-expanded', 'false')
        .append('<span class="icon-bar"></span>')
        .append('<span class="icon-bar"></span>')
        .append('<span class="icon-bar"></span>')
        .appendTo($con.find('.navbar-header'));
    $('<a class="navbar-brand"></a>')
        .attr('href', '#')
        .text('Hi~')
        .appendTo($con.find('div.navbar-header'));
    $('<ul class="nav navbar-nav"></ul>')
        .append('<li><a href="#"><span class="badge badge-tool badge-light">E</span>事件</a></li>')
        .append('<li><a href="#"><span class="badge badge-tool badge-light">$</span>关系</a></li>')
        .appendTo($con.find('.navbar-collapse'));
    $('<ul class="nav navbar-nav navbar-right"></ul>')
        .append('<li><a href="#"><span class="badge badge-tool badge-danger">!</span>退出登录</a></li>')
        .appendTo($con.find('.navbar-collapse'));
}

$(document).ready(function() {
    drawNavbar();
});
