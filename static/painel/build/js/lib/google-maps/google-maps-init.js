function initMap(){var n=new google.maps.LatLng(48.863807,2.339659),o={zoom:4,center:n,mapTypeId:google.maps.MapTypeId.ROADMAP},e=new google.maps.Map(document.getElementById("map_canvas"),o),a=new google.maps.Marker({position:{lat:48.863807,lng:2.339659},map:e,icon:mapMarker}),i={content:"<p><i class='font-icon font-icon-pin'></i>16, Yafo Street, 94142 PARIS</p><p><i class='font-icon font-icon-phone'></i>(+972 2) 629 06 32</p><p><i class='font-icon font-icon-mail'></i>johndoe@gmail.com</p>",disableAutoPan:!1,maxWidth:0,pixelOffset:new google.maps.Size((-140),0),zIndex:null,boxStyle:{width:"280px"},closeBoxURL:"img/close.png",infoBoxClearance:new google.maps.Size(1,1),isHidden:!1,pane:"floatPane",enableEventPropagation:!1};google.maps.event.addListener(a,"click",function(n){t.open(e,this)});var t=new InfoBox(i);t.open(e,a)}function initMap2(){var n=new google.maps.LatLng(38.898526,(-77.036884)),o={zoom:4,center:n,mapTypeId:google.maps.MapTypeId.ROADMAP},e=new google.maps.Map(document.getElementById("map_canvas_2"),o),a=new google.maps.Marker({position:{lat:38.898526,lng:-77.036884},map:e,icon:mapMarker}),i={content:"<p><i class='font-icon font-icon-pin'></i>Pennsylvania Ave NW, Washington, DC 20502, USA</p><p><i class='font-icon font-icon-phone'></i>(+972 2) 629 06 32</p><p><i class='font-icon font-icon-mail'></i>johndoe@gmail.com</p>",disableAutoPan:!1,maxWidth:0,pixelOffset:new google.maps.Size((-140),0),zIndex:null,boxStyle:{width:"280px"},closeBoxURL:"img/close.png",infoBoxClearance:new google.maps.Size(1,1),isHidden:!1,pane:"floatPane",enableEventPropagation:!1};google.maps.event.addListener(a,"click",function(n){t.open(e,this)});var t=new InfoBox(i);t.open(e,a)}function initMap3(){var n=new google.maps.LatLng(1.357974,103.866923),o={zoom:7,center:n,mapTypeId:google.maps.MapTypeId.ROADMAP},e=new google.maps.Map(document.getElementById("map_canvas_3"),o),a=new google.maps.Marker({position:{lat:1.357974,lng:103.866923},map:e,icon:mapMarker}),i={content:"<p><i class='font-icon font-icon-pin'></i>Singapore</p><p><i class='font-icon font-icon-phone'></i>(+972 2) 629 06 32</p><p><i class='font-icon font-icon-mail'></i>johndoe@gmail.com</p>",disableAutoPan:!1,maxWidth:0,pixelOffset:new google.maps.Size((-140),0),zIndex:null,boxStyle:{width:"280px"},closeBoxURL:"img/close.png",infoBoxClearance:new google.maps.Size(1,1),isHidden:!1,pane:"floatPane",enableEventPropagation:!1};google.maps.event.addListener(a,"click",function(n){t.open(e,this)});var t=new InfoBox(i);t.open(e,a)}var mapMarker=new google.maps.MarkerImage("img/google-map-marker.png",new google.maps.Size(28,28),null,null,new google.maps.Size(28,28));$(document).ready(function(){function n(){$(".contacts-page").each(function(){var n=$(this),o=n.find(".box-typical-header"),e=n.find(".contacts-page-col-right:visible"),a=n.find(".map");$(window).width()>700&&(n.hasClass("box-typical-full-screen")?a.height($(window).height()-2-o.outerHeight()):a.height($(window).height()-parseInt($(".page-content").css("padding-top"))-parseInt($(".page-content").css("padding-bottom"))-parseInt(n.css("margin-bottom"))-2-o.outerHeight()),a.height()<e.outerHeight()&&a.height(e.outerHeight()))})}initMap(),n(),$(window).resize(function(){n()}),$('a[href="#tab-contact-1"]').on("shown.bs.tab",function(o){n(),initMap()}),$('a[href="#tab-contact-2"]').on("shown.bs.tab",function(o){n(),initMap2()}),$('a[href="#tab-contact-3"]').on("shown.bs.tab",function(o){n(),initMap3()}),$(".contacts-page").each(function(){var o=$(this),e=o.find(".action-btn-expand"),a="box-typical-full-screen";e.click(function(){o.hasClass(a)?(o.removeClass(a),$("html").css("overflow","auto"),o.find(".tab-content").height("auto").css("overflow","visible"),console.log("close")):(o.addClass(a),$("html").css("overflow","hidden"),o.find(".tab-content").css("overflow","auto").height($(window).height()-2-o.find(".box-typical-header").outerHeight()),console.log("open")),n(),initMap(),initMap2(),initMap3()})})});