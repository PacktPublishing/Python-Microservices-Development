<!DOCTYPE html>
<html>
	<head lang="en">
		<meta charset="UTF-8">
	</head>
	<body>
		<div id="content"></div>
		<script src="/static/react/react.min.js"></script>
		<script src="/static/react-dom.min.js"></script>
		<script src="/static/babel/browser.js"></script>
	
		<script type="text/babel">
			var div =
				<div>
					Hello World
				</div>
			ReactDOM.render(div, document.getElementById('content'));
		</script>
	</body>
</html>