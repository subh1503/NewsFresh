$(document).ready(function() {
    $('a').on('click', function(event) {
        event.preventDefault();
    });

    // JS Function to accquire the csrftoken
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    // JS code to send upvote for a specific news
    $('.fa-smile').on('click', function(event) {
        event.preventDefault();
        var $upvote = $(this);
        var news_id = $(this).parent().attr('id');
        $.ajax({
            url : '',
            type : 'POST',
            data : {
                csrfmiddlewaretoken : csrftoken,
                activity : 'upvote',
                news_id : news_id,
            },
            complete : function(response) {
                if (response.responseJSON == 'valid') {
                    var upvote_count = parseInt($upvote.siblings('.upvote').text(), 10) + 1;
                    $upvote.siblings('.upvote').text(upvote_count.toString());
                }
            }
        });
    });

    // JS code to send downvote for a specific news
    $('.fa-frown').on('click', function(event) {
        event.preventDefault();
        var $downvote = $(this);
        var news_id = $(this).parent().attr('id');
        $.ajax({
            url : '',
            type : 'POST',
            data : {
                csrfmiddlewaretoken : csrftoken,
                activity : 'downvote',
                news_id : news_id,
            },
            complete : function(response) {
                if (response.responseJSON == 'valid') {
                    var downvote_count = parseInt($downvote.siblings('.downvote').text(), 10) + 1;
                    $downvote.siblings('.downvote').text(downvote_count.toString());
                }
            }
        });
    });
});