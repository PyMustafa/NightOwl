$(document).ready(function() {
    $('#show-more-btn').click(function() {
        var url = $(this).data('url');
        $.ajax({
            url: url,
            type: 'GET',
            success: function(response) {
                $('#post-container').append(response.html);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});
