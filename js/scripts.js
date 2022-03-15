window.onload = function()
{
    if(!window.jQuery)
    {
        alert('jQuery not loaded');
    }
    else
    {
        jQuery(document).ready(function(){
            jQuery.get('/js/quotes.txt', function(txt) {
                var quotes = txt.split("\n");
                var randLineNum = Math.floor(Math.random()*(quotes.length));
                jQuery('#quote').append(quotes[randLineNum]);
            });
        });
    }
}

let s = true;

if (window.innerWidth < 768) {
    s = false;
}

function sidebar() {
    if (s == true && window.innerWidth < 768) {
        halfmoon.toggleSidebar();
        s = false;
    } else {
        halfmoon.toggleSidebar();
        s = true;
    }
}

window.onresize = function() {
    if (window.innerWidth >= 768 && s == false) {
        sidebar();
    } else if (window.innerWidth < 768 && s == true) {
        sidebar();
    }
}
