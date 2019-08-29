<?php

// function gen()
// {
//     $ret = yield 'yield1';
//     var_dump($ret);
//     $ret = yield 'yield2';
//     var_dump($ret);
// }

// $gen = gen();
// var_dump($gen->current());
// var_dump($gen->send('ret1'));
// var_dump($gen->send('ret2'));

function gen()
{
    yield "foo";
    yield "bar";
}

$gen = gen();
var_dump($gen->send('something'));
