

$(function () {
   $('.delete-tag-btn').click(function (event) {
      event.preventDefault();
      self = $(this);

      var id = self.attr('data-id');

      zlajax.post({
          'url': '/cms/deltag/',
          'data': {
              'tag_id': id
          },
          'success': function (data) {
              if(data['code'] == 200){
                  window.location.reload();
              } else{
                  console.log(data['message']);
              }
          }
      });

   });
});