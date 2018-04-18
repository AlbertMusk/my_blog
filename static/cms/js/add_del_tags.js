$(function () {
    $('.edit-article-btn').click(function (event) {
        event.preventDefault();
        var self = $(this)

        var modal = $('#myModal');
        var article_id = self.attr('data-id');

        modal.modal('show');



        $('#del-btn').click(function (event) {
            event.preventDefault();

            var tag_name = $("input[name='tag-name']").val();

            zlajax.post({

               'url': '/cms/articles/',
                'data': {
                   'tag_name': tag_name,
                    'operate_id': '0',
                    'article_id': article_id
                },
                'success': function (data) {
                    if(data['code'] == 200){
                        modal.modal('hide');
                        window.location.reload();
                    } else{
                        console.log(data['message']);
                    }
                }

            });


        });


        $('#save-btn').click(function (event) {
            event.preventDefault();

            var tag_name = $("input[name='tag-name']").val();

            zlajax.post({

               'url': '/cms/articles/',
                'data': {
                   'tag_name': tag_name,
                    'operate_id': '1',
                    'article_id': article_id
                },
                'success': function (data) {
                    if(data['code'] == 200){
                        modal.modal('hide');
                        window.location.reload();
                    } else{
                        console.log(data['message']);
                    }
                }

            });


        });
    });
});