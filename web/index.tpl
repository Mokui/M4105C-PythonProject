<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" href="web/bootstrap/css/bootstrap.min.css">

	<script type="text/javascript" src="js/fichier.js"></script>

	<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCCdk4IlO4BT_z6F9EgYWU21eeAaVUpuEs&callback=myMap">
	</script>
</head>

<body>
	<nav class="navbar navbar-inverse " role="navigation">
    <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-2">
            <span class="sr-only">Menu</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">M4105C-Python Project</a>
    </div>
</nav>
<div class="container">
    <div class="page-header">
        <h1>Bienvenue sur la plateforme SportSearch!</h1>
    </div>
	<div class="row">
			<div class="col-md-12">
				<form class="form-horizontal" action="index" method="post">
						<fieldset>
							<legend>Recherche par activité</legend>

							<div class="form-group">
								<label for="example-text-input" class="col-lg-2 control-label">Activité</label>
								<div class="col-lg-2">
										<input class="form-control" type="text" id="example-text-input" name="activity">
								</div>

					            <label for="select" class="col-lg-2 control-label">Ville</label>
					            <div class="col-lg-2">
					            	<select class="form-control" name="city">
						                <option>Nantes</option>
						                <option>Pornic</option>
						                <option>Vertou</option>
						                <option>Carquefou</option>
					                </select>
					            </div>
								<div class="col-lg-2 col-lg-offset-2">
									<button type="submit" class="btn btn-default">Valider</button>
								</div>
			         		</div>
						</fieldset>
				</form>
			</div>
		</div>

		%for installation in dict_installation_equipments :

			<div class="row" style="margin-bottom: 20px;">
				<div class="panel panel-success">
					<!-- Default panel contents -->
				  <div class="panel-heading"><h5>#{{installation.id}} {{installation.name}}</h5></div>
				  <div class="panel-body">
						<span>Informations:</span>
						<ul style="list-style:none;">
							<li><span style="padding:10px;" class="glyphicon glyphicon-flag" aria-hidden="true"></span>{{installation.address}} {{installation.postal_code}} {{installation.city}}
							<li><span style="padding:10px;" class="glyphicon glyphicon-map-marker" aria-hidden="true"></span>latitude {{installation.latitude}} longitude {{installation.longitude}}
						</ul>
				  </div>

					<div class="panel-heading">Equipements</div>
						<div class="panel-body">
							<table class="table">
							  <thead>
							    <tr>
							      <th>#</th>
							      <th>Nom</th>
							      <th>Type</th>
							      <th>Activité</th>
							    </tr>
							  </thead>
							  <tbody>
							%for equipment in dict_installation_equipments[installation] :
								<tr>
								      <th scope="row">{{equipment.id}}</th>
								      <td>{{equipment.name}}</td>
								      <td>{{equipment.familly}}</td>
								      <td>
								      %i = 0
								      %for activity in equipment.activities :
								      	%if(i != 0) :
								      		,
								      	%end
								      	{{activity.name}}
								      %end
								      </td>
								    </tr>
							    <tr>
							%end     
							  </tbody>
							</table>
						</div>
					</div>
				</div>
			%end
		<!--<div class="row">
			<div id="map" style="margin: 0 auto 0 auto;width:90%;height:500px;">OUI LA MAP</div>
		</div>-->

		<div class="modal-body row">
	  </div>
	</div>
</body>
</html>
