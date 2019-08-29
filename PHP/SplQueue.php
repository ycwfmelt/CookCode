<?php

$queue = new SplQueue();
$queue->setIteratorMode(SplQueue::IT_MODE_DELETE);
$queue->enqueue(array("Test","foo"));
