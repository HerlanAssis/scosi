'use strict'
var siadeCtrls = angular.module('siadeControllers', []);
      

siadeCtrls.controller('loginController', ['$scope', '$location', function ($scope, $location) {
 
}])

siadeCtrls.controller('homeCtrl', ['$scope', function($scope) {
	$scope.valor = 1
}])


//lista Bairro
siadeCtrls.controller('bairroCtrl', ['$scope', '$http', '$window', '$location', function($scope,$http,$window,$location) {

	$scope.addBairro = function(){
		$location.path('/cadastrar_bairro/')
	}
	
	$scope.editBairro = function(index){
		console.log('call editBairro()...'+ $scope.bairros[index].id)
		$location.path('/edit_bairro/' + $scope.bairros[index].id);
	}
	
	var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/bairro?depth=2')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.bairros = data;
                        angular.copy($scope.bairros, $scope.copy);
                    });
        }

        load();

        $scope.excluir = function(bairro){
			$http.delete('/api/imoveis/bairro/'+bairro).success(function(data){
				var index = $scope.bairros.indexOf(bairro);
				$scope.bairros.splice(index, 1);
				load()
			});
		
	};
      
}])

//editar Bairro...
siadeCtrls.controller('bairroEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editBairro'+$routeParams.id)
            $http.get('/api/imoveis/bairro/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.bairros = data
                        angular.copy($scope.bairros, $scope.copy);
                    })
        }

        load()

         $scope.bairros = {};

        $scope.updateBairro = function() {
            console.log('updateBairro');
            $http
			.put('/api/imoveis/bairro/' + $scope.bairros.id , $scope.bairros)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/bairros');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}

		 $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});
         
}]);


//cadastrar Bairro...
siadeCtrls.controller('bairro_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	
	$scope.bairro ={};

	$scope.saveBairro = function(){
		
		$http.post('/api/imoveis/bairro/', $scope.bairro)
		.success(function (data){
			$scope.bairros.unshift(data)
			$location.path('/bairros')
		}).error(function(data){
					
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/bairro')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.bairros = data;
                        angular.copy($scope.bairros, $scope.copy);
                    });
        }

        load();

        
         $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});


}])




//listar Agente
siadeCtrls.controller('agenteCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {

	$scope.addAgente = function(){
		$location.path('/cadastrar_agente/')
	}
	
	
	$scope.editAgente = function(index){
		console.log('call editAgente()...'+ $scope.agentes[index].id)
		$location.path('/edit_agente/' + $scope.agentes[index].id);
	}

	var load = function() {
            console.log('call list load()...');
            $http.get('/api/agente/')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.agentes = data;
                        angular.copy($scope.agentes, $scope.copy);
                    });
        }

        load();

        $scope.excluir = function(agente){
			$http.delete('/api/agente/'+agente).success(function(data){
				var index = $scope.agentes.indexOf(agente);
				$scope.agentes.splice(index, 1);
				load()
			});
		
	};
}])

//editar Agente...
siadeCtrls.controller('agenteEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editAgente'+$routeParams.id)
            $http.get('/api/agente/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.agentes = data
                        angular.copy($scope.agentes, $scope.copy);
                    })
        }

        load()

         $scope.agentes = {};

        $scope.updateAgente = function() {
            console.log('updateAgente');
            $http
			.put('/api/agente/' + $scope.agentes.id , $scope.agentes)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/agentes');
				} else {
					$location.path('/agentes');
				}
			}).error(function(data, status, headers, config) {
				
			});

		}

		  $http.get('/api/agente?depth=2')
			.success(function(data, status, headers, config) {
				$scope.tipos = data;
			});

         
}]);


//cadastrar Agente
siadeCtrls.controller('Agente_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.agente ={};

	$scope.saveAgente = function(){
		
		$http.post('/api/agente/', $scope.agente)
		.success(function (data){
			$scope.agentes.unshift(data)
			$location.path('/cidades')
		}).error(function(data){
				
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/agente/')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.agentes = data;
                        angular.copy($scope.agentes, $scope.copy);
                    });
        }

        load();

        $http.get('/api/agente/?depth=2')
			.success(function(data, status, headers, config) {
				$scope.agentes.tipo = data;
			});

		$http.get('/api/agente/')
			.success(function(data, status, headers, config) {
				$scope.tipos = data;
			});

}])







//lista Cidade...
siadeCtrls.controller('cidadeCtrl', ['$scope','$http', '$window', '$location', function ($scope,$http,$window,$location) {
	
	$scope.addCidade = function(){
		$location.path('/cadastrar_cidade/')
	}
	
	$scope.editCidade = function(index){
		console.log('call editCidade()...'+ $scope.municipios[index].id)
		$location.path('/edit_municipio/' + $scope.municipios[index].id);
	}

	
 	
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/municipio')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.municipios = data;
                        angular.copy($scope.municipios, $scope.copy);
                    });
        }

        load();

        $scope.excluir = function(municipio){
			$http.delete('/api/imoveis/municipio/'+municipio).success(function(data){
				var index = $scope.municipios.indexOf(municipio);
				$scope.municipios.splice(index, 1);
				load()
			});
		
	};
}])

//editar Cidade...
siadeCtrls.controller('cidadeEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editCidade'+$routeParams.id)

            $http.get('/api/imoveis/municipio/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.municipios = data
                        angular.copy($scope.municipios, $scope.copy);
                    })
        }

        load()

         $scope.municipios = {};

        $scope.updateCidade = function() {
            console.log('updateCidade');
            $http
			.put('/api/imoveis/municipio/' + $scope.municipios.id , $scope.municipios)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/cidades');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
         
}]);

//cadastrar Cidade...

siadeCtrls.controller('cidade_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.municipio ={};

	$scope.save = function(){
		
		$http.post('/api/imoveis/municipio/', $scope.municipio)
		.success(function (data){
			$scope.municipios.unshift(data)
			$location.path('/cidades')
			}).error(function(data){
				
		})
	
	}

	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/municipio')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.municipios = data;
                        angular.copy($scope.municipios, $scope.copy);
                    });
        }

        load();

         $http.get('/api/imoveis/uf/')
			.success(function(data, status, headers, config) {
				$scope.ufs = data;
			});
}])





//Listar Quadras

.controller('quadraCtrl', ['$scope', '$location', '$http', function($scope,$location, $http) {
	
	$scope.addQuadra = function(){
		$location.path('/cadastrar_quadras')
	}

	$scope.editQuadra = function(index){
		console.log('call editQuadra()...'+ $scope.quadras[index].id)
		$location.path('/edit_quadra/' + $scope.quadras[index].id);
	}

	var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/quadra/?depth=2')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.quadras = data;
                        angular.copy($scope.quadras, $scope.copy);
                    });
        }

        load();

        $scope.excluir = function(quadra){
			$http.delete('/api/imoveis/quadra/'+quadra).success(function(data){
				var index = $scope.quadras.indexOf(quadra);
				$scope.quadras.splice(index, 1);
				load()
			});
	    };

	    $http.get('/api/imoveis/bairro/')
			.success(function(data, status, headers, config) {
				$scope.bairros = data;
			});
}])

//editar Quadra...
siadeCtrls.controller('quadraEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editQuadra'+$routeParams.id)
            $http.get('/api/imoveis/quadra/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.quadras = data
                        angular.copy($scope.quadras, $scope.copy);
                    })
        }

        load()

         $scope.quadras = {};

        $scope.updateQuadra = function() {
            console.log('updateQuadra');
            $http
			.put('/api/imoveis/quadra/' + $scope.quadras.id , $scope.quadras)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/listar_quadras');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
		$http.get('/api/imoveis/bairro/')
			.success(function(data, status, headers, config) {
				$scope.bairros = data;
			});
}]);

//Cadastrar Quadras
siadeCtrls.controller('cadastrar_quadra_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.quadra ={};

	$scope.saveQuadra = function(){
		
		$http.post('/api/imoveis/quadra/', $scope.quadra)
		.success(function (data){
			$location.path('/listar_quadras/')

			}).error(function(data){
			
		})
	
	}


	var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/quadra')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.quadras = data;
                        angular.copy($scope.quadras, $scope.copy);
                    });
        }

        load();

        $http.get('/api/imoveis/bairro/')
			.success(function(data, status, headers, config) {
				$scope.bairros = data;
			});
	
}])

//cadastrar Lado...
siadeCtrls.controller('ladoQuadra_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.lado ={};

	$scope.saveLado = function(){
		
		$http.post('/api/imoveis/lado-quadra/', $scope.lado)
		.success(function (data){
			$scope.lados.unshift(data)
			$location.path('/lado_quadra')
			}).error(function(data){
				
		})
	
	}

	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/lado-quadra/')
                    .success(function(data, status, headers, config) {
                        $scope.lados = data;
                        angular.copy($scope.lados, $scope.copy);
                    });
        }

        load();

        $http.get('/api/imoveis/quadra/')
			.success(function(data, status, headers, config) {
				$scope.quadras = data;
			});


         $http.get('/api/imoveis/logradouro/')
			.success(function(data, status, headers, config) {
				$scope.logradouros = data;
			});   
}])

//Listar Lados
.controller('lado_quadraCtrl', ['$scope', '$location', '$http', function($scope,$location, $http) {
	
	$scope.addLado= function(){
		$location.path('/cadastrar_lado_quadra')
	}

	$scope.editLado = function(index){
		console.log('call editLado()...'+ $scope.lados[index].id)
		$location.path('/edit_lado/' + $scope.lados[index].id);
	}

	var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/lado-quadra/?depth=2')
                    .success(function(data, status, headers, config) {
                        $scope.lados = data;
                        angular.copy($scope.lados, $scope.copy);
                    });
        }

        load();

        $scope.excluir = function(lado){
			$http.delete('/api/imoveis/lado-quadra/'+lado).success(function(data){
				var index = $scope.lados.indexOf(lado);
				$scope.lados.splice(index, 1);
				load()
			});
		
	};
}])

//editar lado...
siadeCtrls.controller('ladoEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editLado'+$routeParams.id)
            $http.get('/api/imoveis/lado-quadra/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        $scope.lados = data
                        angular.copy($scope.lados, $scope.copy);
                    })
        }

        load()

         $scope.lados = {};

        $scope.updateLado = function() {
            console.log('updateLado');
            $http
			.put('/api/imoveis/lado-quadra/' + $scope.lados.id , $scope.lados)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/lado_quadra');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
		$http.get('/api/imoveis/quadra/')
			.success(function(data, status, headers, config) {
				$scope.quadras = data;
			});

		$http.get('/api/imoveis/logradouro/')
			.success(function(data, status, headers, config) {
				$scope.logradouros = data;
			});
}]);



//lista Tipo do Imovel...
siadeCtrls.controller('tipoImovelCtrl', ['$scope','$http', '$location', '$window', function ($scope,$http,$location,$window) {
	  
	  var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/tipo-imovel/?depth=2')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.tipos = data;
                        angular.copy($scope.tipos, $scope.copy);
                    });
        }

        load();

	$scope.addTipoImovel = function(){
		$location.path('/cadastrar_tipo_imovel/')
	}

	$scope.editTipoImovel = function(index){
		console.log('call edittipoImovel()...'+ $scope.tipos[index].id)
		$location.path('/edit_tipoImovel/' + $scope.tipos[index].id);
	}

	$scope.excluir = function(tipo){
			$http.delete('/api/imoveis/tipo-imovel/'+tipo).success(function(data){
				var index = $scope.tipos.indexOf(tipo);
				$scope.tipos.splice(	index, 1);
				load()
			});
		
	};

}])





//cadastrar Imovel...
siadeCtrls.controller('Imovel_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	$scope.imovel ={};

	$scope.saveImovel = function(){
		
		$http.post('/api/imoveis/imovel/', $scope.imovel)
		.success(function (data){
			$scope.imoveis.unshift(data)
			$location.path('/imovel')
		}).error(function(data){
				
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/imovel/')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.imoveis = data;
                        angular.copy($scope.imoveis, $scope.copy);
                    });
       		 }

        load()

        $http.get('/api/imoveis/tipo-imovel/')
			.success(function(data, status, headers, config) {
				$scope.tipos = data;
			});

		$http.get('/api/imoveis/lado-quadra/')
			.success(function(data, status, headers, config) {
				$scope.lados = data;
			});


}])
//lista Imovel...
siadeCtrls.controller('ImovelCtrl', ['$scope','$http', '$location', '$window', function ($scope,$http,$location,$window) {
	  
	  var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/imovel/?depth=2')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.imoveis = data;
                        angular.copy($scope.imoveis, $scope.copy);
                    });
        }

        load();

	$scope.addImovel = function(){
		$location.path('/cadastrar_imovel/')
	}

	$scope.editImovel = function(index){
		console.log('call editImovel()...'+ $scope.imoveis[index].id)
		$location.path('/edit_imovel/' + $scope.imoveis[index].id);
	}

	$scope.excluir = function(imovel){
			$http.delete('/api/imoveis/imovel/'+imovel).success(function(data){
				var index = $scope.imoveis.indexOf(imovel);
				$scope.imoveis.splice(index, 1);
				load()
			});
		 $http.get('/api/imoveis/tipo-imovel/')
			.success(function(data, status, headers, config) {
				$scope.tipos = data;
			});
	};
	$scope.tipos = {
		1: 'Residência',
		2: 'Comércio',
		3: 'Terreno Baldio',
		4: 'Outros'
	};

	 
	 

}])
//editar imovel...
siadeCtrls.controller('imovelEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editImovel'+$routeParams.id)
            $http.get('/api/imoveis/imovel/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        $scope.imoveis = data
                        angular.copy($scope.imoveis, $scope.copy);
                    })
        }

        load()

         $scope.imoveis = {};

        $scope.updateUf = function() {
            console.log('updateImovel');
            $http
			.put('/api/imoveis/imovel/' + $scope.imoveis.id , $scope.imoveis)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/imovel');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
		$http.get('/api/imoveis/lado-quadra/')
			.success(function(data, status, headers, config) {
				$scope.lados = data;
			});

		 $http.get('/api/imoveis/tipo-imovel/')
			.success(function(data, status, headers, config) {
				$scope.tipos = data;
			});

         
}]);





//lista Estado...
siadeCtrls.controller('estadoCtrl', ['$scope','$http', '$location', '$window', function ($scope,$http,$location,$window) {
	  
	  var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/uf')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.ufs = data;
                        angular.copy($scope.ufs, $scope.copy);
                    });
        }

        load();

	$scope.addUf = function(){
		$location.path('/cadastrar_uf/')
	}

	$scope.editUf = function(index){
		console.log('call editUf()...'+ $scope.ufs[index].id)
		$location.path('/edit_uf/' + $scope.ufs[index].id);
	}

	$scope.excluir = function(uf){
			$http.delete('/api/imoveis/uf/'+uf).success(function(data){
				var confirme = alert('tem certeza que quer excluir?')
				if (confirme == true) {
					var index = $scope.ufs.indexOf(uf);
					$scope.ufs.splice(index, 1);
					load()
				}else{
					if (confirme == false) {
						load()
					};
				}
			});
		
	};

}])


//editar Estado...
siadeCtrls.controller('estadoEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editUf'+$routeParams.id)
            $http.get('/api/imoveis/uf/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        $scope.ufs = data
                        angular.copy($scope.ufs, $scope.copy);
                    })
        }

        load()

         $scope.ufs = {};

        $scope.updateUf = function() {
            console.log('updateUf');
            $http
			.put('/api/imoveis/uf/' + $scope.ufs.id , $scope.ufs)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/estados');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
         
}]);

//cadastrar Estado...
siadeCtrls.controller('estado_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	$scope.uf ={};

	$scope.saveUf = function(){
		
		$http.post('/api/imoveis/uf/', $scope.uf)
		.success(function (data){
			$scope.ufs.unshift(data)
			$location.path('/estados')
			 var alert=('Salvo com Sucesso')
		}).error(function(data){
				
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/uf')
                    .success(function(data, status, headers, config) {
                        $scope.ufs = data;
                        angular.copy($scope.ufs, $scope.copy);

                    });
        }

        load()


}])





//lista logradouro...
siadeCtrls.controller('logradouroCtrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	

	$scope.addLogradouro = function(){
		$location.path('/cadastrar_logradouro/')
	}
	$scope.editLogradouro = function(index){
		console.log('call editUf()...'+ $scope.logradouros[index].id)
		$location.path('/edit_logradouro/' + $scope.logradouros[index].id);
	}
		
	$scope.excluir = function(logradouro){
		
			$http.delete('/api/imoveis/logradouro/'+logradouro).success(function(data){
				var index = $scope.logradouros.indexOf(logradouro);
				$scope.logradouros.splice(index, 1);
				load()
			});
		
	};

	 var load = function() {
            $http.get('/api/imoveis/logradouro/?depth=2')
                    .success(function(data, status, headers, config) {
                       
                        $scope.logradouros = data
                        angular.copy($scope.logradouros, $scope.copy)
                    })
        }

        load()

}])


// cadastro Logradouro...
siadeCtrls.controller('logradouro_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	

	$scope.logradouro ={};

	$scope.saveLogradouro = function(){
		
		$http.post('/api/imoveis/logradouro/', $scope.logradouro)
		.success(function (data){
			$scope.logradouros.unshift(data)
			$location.path('/logradouros')
		}).error(function(data){
			
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/imoveis/logradouro/')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.logradouros = data;
                        angular.copy($scope.logradouros, $scope.copy);
                    });
        }

        load();


         $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});


}])

//editar Logradouro...
siadeCtrls.controller('logradouroEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editLogradouro'+$routeParams.id)
            $http.get('/api/imoveis/logradouro/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.logradouros = data
                        angular.copy($scope.logradouros, $scope.copy);
                    })
        }

        load()

         $scope.logradouros = {};

        $scope.updateLogradouro = function() {
            console.log('updateLogradouro');
            $http
			.put('/api/imoveis/logradouro/' + $scope.logradouros.id , $scope.logradouros)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/logradouros');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}

		 $http.get('/api/imoveis/municipio/')
			.success(function(data, status, headers, config) {
				$scope.municipios = data;
			});

}]);

//Cadastrar Ciclo
siadeCtrls.controller('cadastrar_ciclo_Ctrl', ['$scope','$http', '$location', '$filter', '$rootScope', '$routeParams', function ($scope,$http,$location,$filter,$rootScope,$routeParams) {

	$scope.ciclo ={};

	$scope.saveCiclo = function(){
		
		$http.post('/api/trabalhos/ciclo/', $scope.ciclo)
		.success(function (data){
			$scope.ciclos.unshift(data)
			$location.path('/gerenciar_ciclo')
		}).error(function(data){
			
		})
		
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/trabalhos/ciclo/')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.ciclos = data;
                        var ultimoCiclo;
                        $http.get('/api/trabalhos/ciclo/atual/').success(function(ultimo,status,headers,config){
                        	if(ultimo.fechado_em == null){
                        		$location.path("/gerenciar_ciclo")
                        	}
                        });
                        console.log(ultimoCiclo);
                        
                        angular.copy($scope.ciclos, $scope.copy);
                    });
        }

        load();

        $http.get('/api/trabalhos/atividade/')
			.success(function(data, status, headers, config) {
				$scope.atividades = data;
		});

}]);


//Gerenciar Ciclo
siadeCtrls.controller('gerenciar_cicloCtrl', ['$scope','$http', '$location', '$filter', '$rootScope', '$routeParams', function ($scope,$http,$location,$filter,$rootScope,$routeParams) {


	//data do dia...
	//$scope.dataAtual  = $filter('date')(new Date(), 'yyyy-MM-dd');

	$scope.trabalho ={};

	$scope.saveTrabalho = function(){
		//console.log($scope.trabalho.quadra);
		$http.post('/api/trabalhos/trabalho/', $scope.trabalho)
		.success(function (data){
			$scope.trabalhos.unshift(data)/api/trabalhos/atividade/
			$location.path('/gerenciar_ciclo')
		}).error(function(data){
			
		})
		
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/trabalhos/trabalho/')
                    .success(function(data, status, headers, config) {
                        $scope.trabalhos = data;
                        angular.copy($scope.trabalhos, $scope.copy);
                    });
        }

        load();

        $http.get('/api/agente/')
			.success(function(data, status, headers, config) {
				$scope.agentes = data;
			});

		$http.get('/api/imoveis/bairro/')
			.success(function(data, status, headers, config) {
				$scope.bairros = data;
			});

		$http.get('/api/imoveis/quadra/?bairro=1')
			.success(function(data, status, headers, config) {
				$scope.quadras = data;
			});

		$http.get('/api/trabalhos/ciclo/')
			.success(function(data, status, headers, config) {
				$scope.ciclos = data;
			});

		$http.get('/api/trabalhos/ciclo/?last=true')
			.success(function(data, status, headers, config) {
				 var lastKey = Object.keys(data).sort().reverse()[0];
				$scope.ciclo = data[lastKey];				
			});

		

}]);




//cadastrar Atividade
siadeCtrls.controller('Atividade_Cadastro_Ctrl', ['$scope','$http', '$location', function ($scope,$http,$location) {

	$scope.atividade ={};

	$scope.saveAtividade = function(){
		
		$http.post('/api/trabalhos/atividade/', $scope.atividade)
		.success(function (data){
			$scope.atividades.unshift(data)
			$location.path('/atividades')
			
		}).error(function(data){
				
		})
	
	}
		
	 var load = function() {
            console.log('call load()...');
            $http.get('/api/trabalhos/atividade')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.atividades = data;
                        angular.copy($scope.atividades, $scope.copy);
                    });
        }

        load();

}])

//lista Atividade...
siadeCtrls.controller('atividadeCtrl', ['$scope','$http', '$location', function ($scope,$http,$location) {
	

	$scope.addAtividade = function(){
		$location.path('/cadastrar_atividade/')
	}
	$scope.editAtividade = function(index){
		console.log('call editAtividade()...'+ $scope.atividades[index].id)
		$location.path('/edit_atividade/' + $scope.atividades[index].id);
	}
		
	$scope.excluir = function(atividade){
		
			$http.delete('/api/trabalhos/atividade/'+atividade).success(function(data){
				var index = $scope.atividades.indexOf(atividade);
				$scope.atividades.splice(index, 1);
				load()
			});
		
	};

	 var load = function() {
            console.log('call load()...');
            $http.get('api/trabalhos/atividade/')
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.atividades = data
                        angular.copy($scope.atividades, $scope.copy)
                    })
        }

        load()

}])

//editar atividade...
siadeCtrls.controller('atividadeEditCtrl', ['$scope', '$http','$routeParams', '$location', function ($scope, $http, $routeParams,$location) {
      
      var load = function() {
            console.log('load()... editAtividade'+$routeParams.id)
            $http.get('/api/trabalhos/atividade/'+$routeParams.id)
                    .success(function(data, status, headers, config) {
                        console.log(data)
                        $scope.atividades = data
                        angular.copy($scope.atividades, $scope.copy);
                    })
        }

        load()

         $scope.atividades = {};

        $scope.updateAtividade = function() {
          
            $http
			.put('/api/trabalhos/atividade/' + $scope.atividades.id , $scope.atividades)
			.success(function(data, status, headers, config) {
				if(!data.error) {
					$location.path('/atividades');
				} else {
					
				}
			}).error(function(data, status, headers, config) {
				
			});

		}
         
}]);


//Relatorios

siadeCtrls.controller('relatorio_d7', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('relatorio_d1', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('relatorio_ciclo', ['$scope', function($scope) {
	$scope.valor = 1
}])

siadeCtrls.controller('relatorio_pendente', ['$scope', function($scope) {
	$scope.valor = 1
}])



