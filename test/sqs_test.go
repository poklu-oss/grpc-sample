package test

//import "github.com/SQS/micro"
//import "gotest.tools/assert"
import "log"
import (
	"fmt"
	"testing"

	"gotest.tools/assert"
	is "gotest.tools/assert/cmp"
)

func BenchmarkHello(b *testing.B) {
	for i := 0; i < b.N; i++ {
		fmt.Sprintf("hello")
		b.Logf("%d what", i)
	}
}
func TestXXX(t *testing.T) {
	//total := micro.GetDetail()
	log.Printf("hello")
	//assert.Equal(t, 1, 10)
	is.Equal(1, 10)
	total := 10
	if total != 10 {
		t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 10)
	}

}
