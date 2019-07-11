package micro

import (
	"log"
)

func Bar() {
	foo := FooRequest{Foo: 1}
	log.Printf("%v", foo)

}
