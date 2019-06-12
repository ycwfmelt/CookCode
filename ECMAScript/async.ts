async function printDelay(elements: string[]) {
    for (const ele in elements) {
        await delay(400)
        console.log(ele)
    }
}

async function delay(milliseconds: number) {
    return new Promise<void>(resolve => {
        setTimeout(resolve, milliseconds)
    })
}

printDelay(['test1', 'test2', 'test3', 'test4']).then(() => { console.log('print every ele') })
