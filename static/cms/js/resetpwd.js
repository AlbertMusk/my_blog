
$(function () {
    $('#submit').click(function (event) {
       event.preventDefault();

       var oldpwd_input = $("input[name='oldpwd']");
       var newpwd_input = $("input[name='newpwd']");
       var newpwd2_input = $("input[name='newpwd2']");

       var oldpwd = oldpwd_input.val();
       var newpwd = newpwd_input.val();
       var newpwd2 = newpwd2_input.val();

       // data={
       //     'oldpwd': oldpwd,
       //     'newpwd': newpwd,
       //     'newpwd2': newpwd2
       // };
       //
       // var xhr;
       // if(window.XMLHttpRequest){
       //     xhr = new XMLHttpRequest();
       // }else{
       //     xhr = new ActiveXObject('Microsoft.XMLHTTP');
       // }
       //
       // xhr.open('POST','/cms/resetpwd/',true);
       // xhr.send(data);

       zlajax.post({
           'url': '/cms/resetpwd/',
           'data': {
               'oldpwd': oldpwd,
               'newpwd': newpwd,
               'newpwd2': newpwd2
           },
           'success': function (data) {
               if(data['code'] == 200){
                   window.location.reload()
               }
           }
       });

        // $.ajaxSetup({
			// 'beforeSend':function(xhr,settings) {
			// 	if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
        //             var csrftoken = $('meta[name=csrf-token]').attr('content');
        //             xhr.setRequestHeader("X-CSRFToken", csrftoken)
        //         }
			// }
        // });
        //
        // $.ajax({
        //    'type': 'POST',
        //    'url': '/cms/resetpwd/',
        //     'data': {
        //        'oldpwd': oldpwd,
        //         'newpwd': newpwd,
        //         'newpwd2': newpwd2
        //     },
        //     'contentType':'json',
        //     'success': function (data) {
        //         console.log(data);
        //         // window.location.reload();
        //     }
        //
        // });

    });
});