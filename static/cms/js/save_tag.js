

$(function () {
   $('#save-btn').click(function (event) {
       event.preventDefault();

       var modal = $('#myModal')

       var tag_name_input = $("input[name='tag-name']")

       var tag_name = tag_name_input.val();

       zlajax.post({

           'url': '/cms/addtags/',
           'data':{
               'tag_name': tag_name
           },
           'success': function (data) {
               if(data['code'] == 200){
                   modal.modal('hide');
                   window.location.reload();
               } else {
                   console.log(data);
               }
           }

       });

   });
});