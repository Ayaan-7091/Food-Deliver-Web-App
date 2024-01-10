var fcart = document.querySelector('#fcart')
var ftotal = document.querySelector('#ftotal')

function addFood(fid,ftitle,fprice){

    var name = ftitle
    var price = fprice



    var orders = JSON.parse(localStorage.getItem('orders'))
    var total = localStorage.getItem('total')
    var cartSize = orders.length;
    // saving item and total in localstorage
    orders[cartSize]=[name,price]
    localStorage.setItem('orders',JSON.stringify(orders))



    total = Number(total) + Number(price)
    localStorage.setItem('total',total)

    var cart = document.querySelector('#cartNo');
    cart.innerHTML = orders.length;

    // delete button
    fbutton = '<button  class="del" onclick="(removeItem('+cartSize+'))">x</button>'


    ftotal.innerHTML="Total : ₹ "+total;
    fcart.innerHTML +="<li class='orderList'>"+name+ " ₹" +price+ " "+ fbutton+"</li>"
    
}

function fshoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'))
    var total = localStorage.getItem('total')
    var cartSize = orders.length
    fcart.innerHTML=''


    for(let i=0 ; i<cartSize ; i++){
        fbutton = '<button  class="del" onclick="(removeItem('+ i +'))">x</button>'
 
        fcart.innerHTML +="<li class='orderList'>" +orders[i][0]+"  ₹"+orders[i][1] + " "+ fbutton + "</li>"
    }
    ftotal.innerHTML="Total : ₹ "+total;

    var cart = document.querySelector('#cartNo');
    cart.innerHTML = orders.length;
}

fshoppingCart();

function removeItem(n){
  
    // localStorage.clear()


    var orders = JSON.parse(localStorage.getItem('orders'))
    var total = localStorage.getItem('total')
    total = Number(total) - Number(orders[n][1])
    orders.splice(n,1)

    localStorage.setItem('orders',JSON.stringify(orders))
    localStorage.setItem('total',total)
    cart.innerHTML = orders.length;
    var cart = document.querySelector('#cartNo');
    fshoppingCart();

}
