<?php

spl_autoload_register(function ($class_name) {
    require_once $class_name . '.php';
});

function getTaskId()
{
    return new SystemCall(function (Task $task, Scheduler $scheduler) {
        $task->setSendValue($task->getTaskId());
        $scheduler->schedule($task);
    });
};

function task($max)
{
    echo "before yield", PHP_EOL;
    $tid = yield getTaskId();
    echo "after yield", PHP_EOL;
    for ($i = 1; $i <= $max; ++$i) {
        echo "This is task $tid iteration $i.\n";
        yield;
    }
}

$scheduler = new Scheduler;

$scheduler->newTask(task(10));
$scheduler->newTask(task(5));

// $scheduler->run();
