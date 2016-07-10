/**
 * Created by xiaozhiqi on 16-7-10.
 */

KindEditor.ready(function(K) {
        K.create('textarea[name=content]',{
            width:'800px',
            height:'500px',
            uploadJson: '/admin/upload/kindeditor',
        });
    });
