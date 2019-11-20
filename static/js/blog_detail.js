

        $("#commit_form").submit(function () {
            CKEDITOR.instances['id_text'].updateElement();

             $.ajax({
                url:"/commit/commit_submit",
                type:'POST',
                data:$(this).serialize(),
                cache:false,

                success:function (data) {
                    console.log(data);
                    if(data['statue']=="SUCCESS")
                    {
                        // 插入数据
                        if ($('#reply_comment_id').val() == 0){
                            var comment_html = '<div id = "root_'+data['pk']+'"class="comment">'+
                            '<span>' + data['username']+ '</span> <span>(' + data['commit_time'] +
                            ' ):</span> <div id ="commit_'+ data['pk']+'">'+
                            data['text'] + '</div><a href="javascript:reply('+data['pk']+');">回复</a> </div>';

                        $("#commit_list").prepend(comment_html);

                        }else {
                           var reply_html = '<div class="reply">' +
                            '<span>'+data['username']+'</span>'+
                            '<span>('+ data['commit_time'] +')回复{{ commit.user.username }}:</span>' +
                            '<br><div id ="commit_'+data['pk']+'">' +
                            data['text'] + '</div>' +
                            '<a href="javascript:reply('+data['pk']+');">回复</a></div>';
                            $("#root_"+data['root_pk']).append(reply_html);

                        }
                            CKEDITOR.instances['id_text'].setData('');
                            $("#reply_response").hide();
                            $('#reply_comment_id').val('0');
                    }else {
                        $("#comment_error").text(data['message']);
                    }
                },
                error:function (xhr) {
                    console.log(xhr);
                }

            });
            return false;
        });
        function reply(reply_id) {
            $("#reply_comment_id").val(reply_id);
            var html=$("#commit_"+ reply_id).html();
            $("#reply_content").html(html);
            $("#reply_response").show();

            $('html').animate({scrollTop:$("#commit_form").offset().top-60}, 300, function () {
                CKEDITOR.instances['id_text'].focus();
            })
        }
        function likeChange(obj, content_type, object_id){
            var is_like = obj.getElementsByClassName('active').length == 0;
            $.ajax({
                url:"/like/like_change",
                type:'GET',
                data:{
                    content_type:content_type,
                    object_id:object_id,
                    is_like:is_like
                },
                cache:false,
                 success:function (data) {
                     if(data['status']=='SUCCESS'){
                        // 更新点赞状态
                        var element = $(obj.getElementsByClassName('glyphicon'));
                        if(is_like){
                            element.addClass('active');
                        }else{
                            element.removeClass('active');
                        }
                        // 更新点赞数量
                        var liked_num = $(obj.getElementsByClassName('like_num'));
                        liked_num.text(data['like_num']);
                    }else{
                        alert(data['message']);
                    }
                },
                error:function (xhr) {
                    console.log(xhr);
                }});

        }