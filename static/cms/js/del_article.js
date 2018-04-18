
$(function () {
    $('.delete-article-btn').click(function (event) {
        event.preventDefault();


        var article_id = $(this).attr('data-id')

        zlajax.post({
            'url': '/cms/delarticle/',
            'data': {
                'article_id': article_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    window.location.reload();
                    alert('success');
                } else {
                    console.log(data['message']);
                }
            }
        })

    });
});