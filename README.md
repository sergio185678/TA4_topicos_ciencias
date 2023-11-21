# TF_topicos_ciencias
<div style="width: 100%; clear: both;">
<div style="float: center; width: 50%;">
<img src="/assets/upc_logo.png", align="center" style="height: 150px; width: 400px;>
</div>

<div style="float: right; width: 50%;">
<h5 style="margin: 0; padding-top: 22px; text-align:center;">Trabajo Final </h5>
<h5 style="margin: 0; padding-top: 22px; text-align:center;">Tópicos en Ciencias de la Computación </h5>
<div>
<h5 style="margin: 0; padding-top: 22px; text-align:center;">Integrantes: </h5>

<p>Santisteban Cerna, Jose Mauricio - U201922760</p>
<p>Paredes Villagra, Renzo Arturo - U20191b335</p>
<p>Flores Ñahuis, Sergio Andres - U201915474</p>
</div>


<h5 style="margin: 0; padding-top: 22px; text-align:center;">Profesor: </h5>
<p style="margin: 0; text-align:center;">Canaval Sánchez, Luis Martin</p>
<p style="margin: 0; text-align:center;">Noviembre 2023</p>
</div>
<div style="width:100%;">&nbsp;</div>
<p>------------------------------------------------------------------------------------------------------------------------</p>
#Indice

1. [Definición del problema y motivación](#data1)
2. [Objetivos](#data2)
3. [Metodología](#data3)
4. [Implementación](#data4)
5. [Referencias Bibliográficas](#data5)

#### 1. Definición del problema y motivación <a name="data1"></a>
El transporte interprovincial es un medio importante para la mayoría de peruanos que va más allá del hecho de movilizarse para vacacionar. Para el 2021, en plena reactivación económica de este sector, se realizaron más de 750 mil viajes movilizando más de 43 millones de personas, siendo los viajes interregionales e interprovinciales los que más gente transportó (TV Perú Noticias, 2021). Durante las protestas por la inestabilidad política, este sector se vio afectado por el cierre de carreteras y la reducción de las rutas de circulación. Además, se estima que cerca de mil empresas se habrían visto afectadas por esto (Mamani, 2023). De por sí, las rutas de transporte para vehículos interprovinciales no cumplen con todos los estándares de calidad o se encuentran en zonas de difícil acceso o que representan un riesgo para la vida de los pasajeros. Es por ello que comprender cómo se pueden encontrar rutas con un acceso más sencillo es importante para permitir que el transporte interprovincial funcione de la mejor manera posible.

#### 2. Objetivos  <a name="data2"></a>
El principal objetivo de este hito es implementar un sistema multiagentes apoyándonos en lo aprendido en el curso para que estos aprendan a escoger las rutas más sencillas para movilizarse.
#### 3. Metodología  <a name="data3"></a>
La metodología a utilizar es la de Python Agent Development Framework o PADE por sus siglas en inglés. Se utilizaron las librerías Qt para implementar la comunicación entre las redes de nodos y la creación de la GUI.
#### 4. Implementación  <a name="data4"></a>
 [GUI](/gui.py)
 [Variables Globales](/globals.py)
 [Agente como vehículo interprovincial](/truckagent.py)
 [Host Agent](/hostagent.py)

#### 5. Referencias Bibliográficas  <a name="data5"></a>
Mamani, M. (30 de enero de 2023). Las pérdidas millonarias del transporte interprovincial y el vía crucis que padecen los pasajeros para poder viajar. Infobae. Recuperado el 20 de noviembre de 2023 de: https://www.infobae.com/peru/2023/01/30/las-perdidas-millonarias-del-transporte-interprovincial-y-el-via-crucis-que-padecen-los-pasajeros-para-poder-viajar/ 
TV Perú Noticias. (23 de octubre de 2021). Transporte interprovincial: cerca de 800 mil viajes fueron realizados en todo lo que va del 2021. TV Perú. Recuperado el 20 de noviembre de 2023 de: https://www.tvperu.gob.pe/noticias/nacionales/transporte-interprovincial-cerca-de-800-mil-viajes-fueron-realizados-en-todo-lo-que-va-del-2021 
