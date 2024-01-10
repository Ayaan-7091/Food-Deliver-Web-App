var hours = 24;
var now = new Date().getTime();
console.log(now)
var stepTime = localStorage.getItem('stepTime')


if (stepTime==null){
    localStorage.setItem('stepTime',now)
}
else{
    if(now-stepTime > hours*60*60*1000){
        localStorage.clear()
        localStorage.setItem('stepTime',now)

    }
}


var orders = JSON.parse(localStorage.getItem('orders'))
var total = localStorage.getItem('total')


if (orders === null || orders === undefined){
    localStorage.setItem('orders',JSON.stringify([]))
    var orders = JSON.parse(localStorage.getItem('orders'))

}

if (total === null || total === undefined){
    localStorage.setItem('total',0)
    var total = localStorage.getItem('total')


}




