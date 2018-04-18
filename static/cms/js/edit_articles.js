
$(function () {
    $('#edit-article-btn').click(function (event) {
        event.preventDefault();

        var title = $("input[name='title']").val();
        var summary = $("input[name='summary']").val();

        var checked = $('input[type=checkbox]:checked');

        var tag_name = new Array();
        var tags = {};

        $.each(checked,function (k,v) {
            tag_name.push(v.name);
        });

        var length = tag_name.length;
        console.log(length);

        for(var i = 0;i < length;i++){
            tags[tag_name[i]] = tag_name[i];
        }
        console.log(tags);


        var context = testEditor.getMarkdown();

        zlajax.post({
            'content-type':json,
            'url': '/cms/earticle/',
            'data': {
                'title': title,
                'summary': summary,
                'context': context
            },
            'success': function (data) {
                if(data['code'] == 200){
                    alert('success!');
                    window.location.reload();
                } else {
                    alert(data['message']);
                }
            }
        })

    });
});