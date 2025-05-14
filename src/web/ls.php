<?php
$directory = '/root';
foreach (new DirectoryIterator($directory) as $fileInfo) {
    if (!$fileInfo->isDot()) {
        echo $fileInfo->getFilename() . PHP_EOL;
    }
}
?>