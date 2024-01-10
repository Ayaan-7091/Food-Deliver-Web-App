
var fname = document.querySelector('#name')
var fprice = document.querySelector('#price')
var fbutton = document.querySelector('#fbutton')



function shoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'))
    var total = localStorage.getItem('total')
    var cartSize = orders.length;
    fname.innerHTML='';
    fprice.innerHTML='';
    fbutton.innerHTML='';


    for(let i=0 ; i<cartSize ; i++){
        fbutton.innerHTML +='<button  class="del" onclick="(removeItem('+ i +'))">x</button>'+"<br>";
 
        fname.innerHTML +=orders[i][0]+"<br>";
        fprice.innerHTML += "₹"+orders[i][1]+"<br>";
    }
    ftotal.innerHTML="Order Total : ₹ "+total;

    var cart = document.querySelector('#cartNo');
    cart.innerHTML = orders.length;
}

shoppingCart();

function removeItem(n){
  
    // localStorage.clear()


    var orders = JSON.parse(localStorage.getItem('orders'))
    var total = localStorage.getItem('total')
    total = Number(total) - Number(orders[n][1])
    orders.splice(n,1)

    localStorage.setItem('orders',JSON.stringify(orders))
    localStorage.setItem('total',total)
    var cart = document.querySelector('#cartNo');
    cart.innerHTML = orders.length;
    shoppingCart();

}


var note = document.querySelector('#deliveryText')


function order(){
    
    var msg = note.value
    var ur = 'order';
    var orders = localStorage.getItem('orders')

    var orderData = {};
    orderData['orders']=orders
    orderData['note']=msg
    
    var orderLength = orderData.length;
    // alert(msg.length)

    if (orders.length > 2 ) {

        if(msg.length>0){
    $.ajax({
        url:ur,
        type:"POST",
        data : orderData,
        success:function(data){
            
            window.location.replace('/success')
            localStorage.setItem('orders',JSON.stringify([]))
            localStorage.setItem('total',0)
            
        
           
        


        }

    })}
    else{
        alert("Please Specify a Delivery Address")
    }

}

else {
    alert("You Cart Is Empty")
}
    

};

