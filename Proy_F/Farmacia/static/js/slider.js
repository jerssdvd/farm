var fotos = ['{% static "img/nat.jpg" %}','{% static "img/pildor.jpg" %}','{% static "img/fondo3.jpg" %}','{% static "img/fondo3.jpg" %}'];
var posiciones = ['{% static "img/posicion.png" %}','{% static "img/posdos.png" %}','{% static "img/postres.png" %}','{% static "img/poscuatro.png" %}'];
var atxt1 = ['<p class="slaiderttxtuno foto1"> Foto 1</p>','<p class="slaiderttxtuno foto2"> Foto 2</p>','<p class="slaiderttxtuno foto3"> Foto 3</p>','<p class="slaiderttxtuno foto4"> Foto 4</p>'];
var atxt1 = ['<p class="slaiderttxtdos"> Foto 1</p>','<p class="slaiderttxtdos"> Foto 2</p>','<p class="slaiderttxtdos"> Foto 3</p>','<p class="slaiderttxtdos"> Foto 4</p>'];
var marcador=0;
var seg=3;

var elementGaleria= document.getElementById('galeriaimg');
var elementpunto= document.getElementById('puntosprimeros');
var elementtexto1= document.getElementById('letrerouno');
var elementtexto2= document.getElementById('letrerodos');

function Slaiderac(){
	elementGaleria.setAttribute("src",fotos[marcador]);
	elementpunto.setAttribute('src',posiciones[marcador]);
	elementtexto1.innerHTML = atxt1[marcador];
	elementtexto2.innerHTML = atxt2[marcador];
	
	if(marcador<fotos.length-1){
		marcador++;
	}else {
		marcador=0;
	}
	setTimeout(Slaiderac,seg*1000);
}
Slaiderac();