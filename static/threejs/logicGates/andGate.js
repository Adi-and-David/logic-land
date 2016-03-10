// Still need to add a general size parameter
AndGate = function(){
  var group = new THREE.Group();
  var geometryCylinder = new THREE.CylinderGeometry( 500, 500, 100, 320 );
  var gateMaterial = new THREE.MeshBasicMaterial( {color: 0x999966} );
  var cylinder = new THREE.Mesh( geometryCylinder, gateMaterial );

  var geometrySquare = new THREE.BoxGeometry(700,100,1000);
  var square = new THREE.Mesh(geometrySquare, gateMaterial);

/*
  ********************************************************************
  Add this to a class of its own
  ********************************************************************
*/
  var wireGroup = new THREE.Group();
  var wireMaterial = new THREE.MeshBasicMaterial( {color: 0xD3D3D3} );
  var geometryLeftWire = new THREE.CylinderGeometry(30,30,500,100);
  var geometryRightWire = new THREE.CylinderGeometry(30,30,500,100);
  var geometryFrontWire = new THREE.CylinderGeometry(30,30,500,100);
  var leftWire = new THREE.Mesh( geometryLeftWire, wireMaterial );
  var rightWire = new THREE.Mesh( geometryRightWire,wireMaterial );
  var frontWire = new THREE.Mesh ( geometryFrontWire,wireMaterial );


  frontWire.position.set(-450,0,0);
  frontWire.rotation.z = Math.PI/2;

  leftWire.position.set(700,0,300);
  leftWire.rotation.z = Math.PI/2;

  rightWire.position.set(700,0,-300);
  rightWire.rotation.z = Math.PI/2;
  wireGroup.add(leftWire);
  wireGroup.add(rightWire);
  wireGroup.add(frontWire);
/*
  ********************************************************************
  ********************************************************************
*/

  square.position.set(350,0,0);


  group.add(wireGroup);

  group.add(leftWire);
  group.add(rightWire);
  group.add(frontWire);
  group.add(square);
  group.add(cylinder);
  return group;
}
