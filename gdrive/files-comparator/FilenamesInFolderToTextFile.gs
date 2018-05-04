
function listFolderFileNamesToTextFile() {
  var foldername = '???'; // => https://drive.google.com/drive/folders/???
  var output_file_id = '???' ; // => https://docs.google.com/document/d/????-???-???
  var output_file  = DriveApp.getFileById(output_file_id); 
  var output_filenames = '';
  
  var folders = DriveApp.getFolderById(foldername)  
  var contents = folders.getFiles();  
 
  var file;
  var name;  
  
  while(contents.hasNext()) {
    file = contents.next();
    name = file.getName();          
    output_filenames = name+'\n' + output_filenames;    
  }    
  output_file.setContent(output_filenames);
};