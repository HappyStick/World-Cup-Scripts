#include json2.js

// All global variables
var javascriptPath = "F:/World Cup/2018 - Current cup/Scripts/mappool_cards";
var mappoolCardPath = "F:/World Cup/2018 - Current cup/Scripts/Resources/Maps/Showcase"

var doc = app.activeDocument.layerSets.getByName("master");
var currentLayer = doc.activeLayer;

var nmLayer = doc.artLayers.getByName("nm");
var hdLayer = doc.artLayers.getByName("hd");
var hrLayer = doc.artLayers.getByName("hr");
var dtLayer = doc.artLayers.getByName("dt");
var fmLayer = doc.artLayers.getByName("fm");
var tbLayer = doc.artLayers.getByName("tb");

var textLayers = doc.layerSets.getByName("text");
var songNameLayer = textLayers.artLayers.getByName("song_name");
var songNameLayer50 = textLayers.artLayers.getByName("song_name_50");
var artistDiffNameLayer = textLayers.artLayers.getByName("artist_diff_name");
var mapperNameLayer = textLayers.artLayers.getByName("mapper_name");

// Loads the json into showcase and runs the script showcase.length times
(function main(){

    var showcase = loadJson('showcase.json');

    file = app.openDialog();

    for (var i = 0; i < showcase.length; i++){
        var show = showcase[i];
        textManipulation(show);
    }
})();

// Loads the json into memory
function loadJson(relPath){

    var script = new File($.fileName);
    var jsonFile = new File(script.path + '/' + relPath);

    jsonFile.open('r');
    var str = jsonFile.read();
    jsonFile.close();

    return JSON.parse(str);
}

// Does the text changes & additions for each mappool card
function textManipulation(show){
	songNameLayer.visible = false;
	songNameLayer50.visible = false;
	if (show.title.length > 50){
		songNameLayer50.visible = true;
		songNameLayer50.textItem.contents = show.title;
	}
	else{
		songNameLayer.visible = true;
		songNameLayer.textItem.contents = show.title;
	}
	artistDiffNameLayer.textItem.contents = show.artist + "     " + "[" + show.difficulty + "]";
	mapperNameLayer.textItem.contents = show.mapper;

	importIMG(show);
}

// Turns all the mappool images into their _default.png 
function importIMG(show){
	app.load(file[parseInt(show.map_number - 1)]);
	newImage = app.activeDocument;
	newImage.selection.selectAll();
	newImage.selection.copy();
	newImage.close(SaveOptions.DONOTSAVECHANGES);
	var imgLayerRef = doc.layerSets.getByName("temp").artLayers.add();
	imgLayerRef.name = "image_" + show.map_number;
	app.activeDocument.paste();
	var imgLayerSetRef = doc.layerSets.getByName("image");
	imgLayerSetRef.visible = true;
	doc.layerSets.getByName("temp").artLayers[0].duplicate(imgLayerSetRef).name = "bg";
	var bgLayer = doc.layerSets.getByName("image").layers[0];
	bgLayer.grouped = true;
	bgLayer.opacity = 35;
	doc.layerSets.getByName("temp").visible = false;
	doc.layerSets.getByName("bw_filter").visible = false;
	doc.opacity = 100;

	if (show.mod == "NM"){
		nmLayer.visible = true;
	}
	else if (show.mod == "HD"){
		hdLayer.visible = true;
	}
	else if (show.mod == "HR"){
		hrLayer.visible = true;
	}
	else if (show.mod == "DT"){
		dtLayer.visible = true;
	};
	else if (show.mod == "FM"){
		fmLayer.visible = true;
	};
	else if (show.mod == "TB"){
		tbLayer.visible = true;
	};

	savePNG_default(parseInt(show.map_number - 1) + '_default', show);

}

function savePNG_default(name, show){
	var doc = app.activeDocument;
    var file = new File(mappoolCardPath + '/' + name + '.png');

    var options = new PNGSaveOptions();
    options.quality = 5;

    doc.saveAs(file, options, true);

    blackWhite(show);
}

// Changes the _default variant into the _bw variant
function blackWhite(show){
	var doc = app.activeDocument.layerSets.getByName("master");
	var imgLayerSetRef = doc.layerSets.getByName("image");
	var bwLayerSetRef = doc.layerSets.getByName("bw");
	doc.layerSets.getByName("temp").visible = true;
	doc.layerSets.getByName("bw_filter").visible = true;
	imgLayerSetRef.visible = false;
	bwLayerSetRef.visible = true;
	doc.layerSets.getByName("temp").artLayers[0].duplicate(bwLayerSetRef).name = "bw_bg";
	var bwLayer = doc.layerSets.getByName("bw").artLayers[0];
	bwLayer.grouped = true;
	bwLayer.opacity = 35;
	doc.layerSets.getByName("temp").visible = false;
	doc.opacity = 50;

	savePNG_bw(parseInt(show.map_number - 1) + '_bw', show);
}

function savePNG_bw(name, show){
	var doc = app.activeDocument;
    var file = new File(mappoolCardPath + '/' + name + '.png');

    var options = new PNGSaveOptions();
    options.quality = 5;

    doc.saveAs(file, options, true);

    teamRed(show);
}

// Changes the _bw variant into the _red variant
function teamRed(show){
	var doc = app.activeDocument.layerSets.getByName("master");
	var imgLayerSetRef = doc.layerSets.getByName("image");
	var bwLayerSetRef = doc.layerSets.getByName("bw");
	var redLayerSetRef = doc.layerSets.getByName("red");
	doc.layerSets.getByName("temp").visible = true;
	doc.layerSets.getByName("bw_filter").visible = false;
	imgLayerSetRef.visible = false;
	bwLayerSetRef.visible = false;
	redLayerSetRef.visible = true;
	doc.layerSets.getByName("temp").artLayers[0].duplicate(redLayerSetRef).name = "red_bg";
	var redLayer = doc.layerSets.getByName("red").artLayers[0];
	redLayer.grouped = true;
	redLayer.opacity = 35;
	doc.layerSets.getByName("temp").visible = false;

	savePNG_red(parseInt(show.map_number - 1) + '_red', show);
}

function savePNG_red(name, show){
	var doc = app.activeDocument;
    var file = new File(mappoolCardPath + '/' + name + '.png');

    var options = new PNGSaveOptions();
    options.quality = 5;

    doc.saveAs(file, options, true);
    teamBlue(show);
}

// Changes the _red variant into the _blue variant
function teamBlue(show){
	var doc = app.activeDocument.layerSets.getByName("master");
	var imgLayerSetRef = doc.layerSets.getByName("image");
	var bwLayerSetRef = doc.layerSets.getByName("bw");
	var redLayerSetRef = doc.layerSets.getByName("red");
	var blueLayerSetRef = doc.layerSets.getByName("blue");
	doc.layerSets.getByName("temp").visible = true;
	doc.layerSets.getByName("bw_filter").visible = false;
	imgLayerSetRef.visible = false;
	bwLayerSetRef.visible = false;
	redLayerSetRef.visible = false;
	blueLayerSetRef.visible = true;
	doc.layerSets.getByName("temp").artLayers[0].duplicate(blueLayerSetRef).name = "blue_bg";
	var blueLayer = doc.layerSets.getByName("blue").artLayers[0];
	blueLayer.grouped = true;
	blueLayer.opacity = 35;
	doc.layerSets.getByName("temp").visible = false;

	savePNG_blue(parseInt(show.map_number - 1) + '_blue', show);
}

function savePNG_blue(name, show){
	var doc = app.activeDocument;
    var file = new File(mappoolCardPath + '/' + name + '.png');

    var options = new PNGSaveOptions();
    options.quality = 5;

    doc.saveAs(file, options, true);
    resetDoc();
}

// Resets everything for the next image to be loaded in
function resetDoc(){
	var doc = app.activeDocument.layerSets.getByName("master");
	var bgLayer = doc.layerSets.getByName("image").layers[0];
	doc.opacity = 100;
	bgLayer.remove();
	var bwLayer = doc.layerSets.getByName("bw").layers[0];
	bwLayer.remove()
	var redLayer = doc.layerSets.getByName("red").layers[0];
	redLayer.remove()
	var blueLayer = doc.layerSets.getByName("blue").layers[0];
	blueLayer.remove()
	var imgLayerSetRef = doc.layerSets.getByName("image");
	var bwLayerSetRef = doc.layerSets.getByName("bw");
	var redLayerSetRef = doc.layerSets.getByName("red");
	var blueLayerSetRef = doc.layerSets.getByName("blue");
	doc.layerSets.getByName("temp").visible = true;
	imgLayerSetRef.visible = true;
	bwLayerSetRef.visible = false;
	redLayerSetRef.visible = false;
	blueLayerSetRef.visible = false;
	nmLayer.visible = false;
	hdLayer.visible = false;
	hrLayer.visible = false;
	dtLayer.visible = false;
	fmLayer.visible = false;
	tbLayer.visible = false;
}