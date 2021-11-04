
var API_URL = window.location.origin + "/gis"
const reja = [{ "sum": 53000, "viloyat_id": 1 }, { "sum": 76000, "viloyat_id": 2 }, { "sum": 60600, "viloyat_id": 3 }, { "sum": 93500, "viloyat_id": 4 }, { "sum": 140000, "viloyat_id": 5 }, { "sum": 38039, "viloyat_id": 6 }, { "sum": 67750, "viloyat_id": 7 }, { "sum": 94230, "viloyat_id": 8 }, { "sum": 90800, "viloyat_id": 9 },{ "sum": 80000, "viloyat_id": 10 }, { "sum": 103845, "viloyat_id": 11 }, { "sum": 99500, "viloyat_id": 12 }, { "sum": 33200, "viloyat_id": 13 }, { "sum": 1561, "viloyat_id": 14 } ]


function reja_find(arr,vil_id){
    console.log(arr);
    for(var i=0; i<arr.length; i++){
        console.log(arr[i].viloyat_id, vil_id);
        if(arr[i].viloyat_id==vil_id) return arr[i]['sum'];
    }
    return 0;
}

$(document).ready(function(){



    $.ajax({
        url: API_URL + "/monitoring",
        type : "GET",
        success: function(crops) {
            let html = "";
            const table_data = document.getElementById('data');
            var ffs = 0;
            crops.map(crop => {
                let id = crop.viloyat_id;
                var ff = reja_find(reja, crop.viloyat_id);
                ffs +=ff;                 
                var farqi = ff-crop.sum;
                let viloyat =
                    html = html +  `
                <tr class="viloyat" data-id="${crop.viloyat_id}" >
                    <td>${crop.viloyat_id}</td>
                    <td><a href='${API_URL}/page/monitoring/${crop.viloyat_id}'> ${crop.viloyat}</a></td>
                    <td>${ff.toFixed(0)}  </td>
                    <td>${crop.sum.toFixed(1)}</td>
                    <td>${crop.sum_today.toFixed(1)}</td>
                    <td>${farqi.toFixed(1)}</td>
                </tr>
                `
        
            });
            var sum_total = crops.reduce(function(sum, current) {
                return sum + current.sum;
                }, 0);
            var sum_today_total = crops.reduce(function(sum, current) {
                return sum + current.sum_today;
                }, 0);
            var ss = ffs - sum_total;
            html = html +  `
            <tr>
                <td colspan="2" ><b>Жами:</b></td>
                <td><b>${ffs}</b> </td>
                <td><b>${sum_total.toFixed(0)}</b> </td>
                <td><b>${sum_today_total.toFixed(1)}</b> </td>
                <td><b>${ss.toFixed(0)}</b> </td>
            </tr>
            `


            table_data.innerHTML = html
        },
        complete : function () {
            $(".viloyat").click(function(){
                            });
        }
    });

    
  


    
    
})

