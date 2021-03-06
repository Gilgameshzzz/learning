//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);

    $.get("/order/my_order/", function (data) {
        if (data.code == 200){
            var order_temp = template('order_temp_script', {orders: data.order_house});
            $('.orders-list').html(order_temp);
        };
         $(".order-accept").on("click", function(){
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-accept").attr("order-id", orderId);

    });
        $(".order-reject").on("click", function(){
            var orderId = $(this).parents("li").attr("order-id");
            $(".modal-reject").attr("order-id", orderId);
    });
    });
    $(".modal-accept").on("click",function () {
        var order_id = $('.modal-accept').attr('order-id')
        $.ajax({
            url:'/order/order_status/',
            type:'POST',
            data:{'order_id':order_id, 'status': "WAIT_PAYMENT"},
            dataType:'json',
            success:function (data) {
                if (data.code == 200){
                    window.location.reload()
                }
            }
        })
    });
    $(".modal-reject").on("click",function () {
        var order_id = $('.modal-reject').attr('order-id')
        var comment = $('#reject-reason').val()
        $.ajax({
            url:'/order/order_status/',
            type:'POST',
            data:{'order_id':order_id, 'status': "REJECTED", 'comment':comment},
            dataType:'json',
            success:function (data) {
                if (data.code == 200){
                    window.location.reload()
                }
            }
        })
    });
})