<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" href="web/bootstrap/css/bootstrap.min.css">
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
				<form class="form-horizontal" action="search" method="post">
						<fieldset>
							<legend>Recherche par activité</legend>

							<div class="form-group">
									<label for="example-text-input" class="col-lg-2 control-label">Activité</label>
									<div class="col-lg-2">
											<input class="form-control" type="text" id="example-text-input">
									</div>

		              <label for="select" class="col-lg-2 control-label">Ville</label>
		              <div class="col-lg-2">
		                  <select class="form-control" name="activite">
		                      <option>Nantes</option>
		                      <option>Paris</option>
		                      <option>Lyon</option>
		                      <option>Gland</option>
		                      <option>New York</option>
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

	<div class="row">
		<div class="panel panel-success">
			<!-- Default panel contents -->
		  <div class="panel-heading"><h5>#2543541 Complexe sportif</h5></div>
		  <div class="panel-body">
				<span>Informations:</span>
				<ul style="list-style:none;">
					<li><span style="padding:10px;" class="glyphicon glyphicon-flag" aria-hidden="true"></span>Beaulieu 44000 Nantes
					<li><span style="padding:10px;" class="glyphicon glyphicon-map-marker" aria-hidden="true"></span>latitude 000 longitude 000
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
					    <tr>
					      <th scope="row">1</th>
					      <td>Mark</td>
					      <td>Otto</td>
					      <td>@mdo</td>
					    </tr>
					    <tr>
					      <th scope="row">2</th>
					      <td>Jacob</td>
					      <td>Thornton</td>
					      <td>@fat</td>
					    </tr>
					    <tr>
					      <th scope="row">3</th>
					      <td>Larry</td>
					      <td>the Bird</td>
					      <td>@twitter</td>
					    </tr>
					  </tbody>
					</table>
				</div>
		</div>
	</div>


	<div class="modal-body row">
  </div>
</div>
</body>
</html>
