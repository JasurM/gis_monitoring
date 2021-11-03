
var API_URL = window.location.origin + "/api"


const reja = [{ "sum": 4.470000000000001, "viloyat_id": 1 }, { "sum": 172.86, "viloyat_id": 2 }, { "sum": 19.27, "viloyat_id": 3 }, { "sum": 172.61, "viloyat_id": 4 }, { "sum": 52.79, "viloyat_id": 5 }, { "sum": 250.94, "viloyat_id": 6 }, { "sum": 27.93, "viloyat_id": 7 }, { "sum": 1.9, "viloyat_id": 8 }, { "sum": 34, "viloyat_id": 9 }, { "sum": 12.68, "viloyat_id": 11 }, { "sum": 46.65, "viloyat_id": 12 } ]


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
            crops.map(crop => {
                let id = crop.viloyat_id;
                var ff = reja_find(reja, crop.viloyat_id);
                var farqi = ff-crop.sum;
                let viloyat =
                    html = html +  `
                <tr>
                    <td>${crop.viloyat_id}</td>
                    <td>${crop.viloyat}</td>
                    <td>${ff.toFixed(2)}  </td>
                    <td>${crop.sum.toFixed(2)}</td>
                    <td>${crop.sum_today.toFixed(2)}</td>
                    <td>${farqi.toFixed(2)}</td>
                </tr>
                `
        
            });
            table_data.innerHTML = html
        } 
    });

    
  


    
    
})

