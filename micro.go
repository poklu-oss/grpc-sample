package main

import (
	pb "SQS/gogen/micro"
	"context"

	// "encoding/json"
	//	"errors"
	"fmt"
	"log"

	// "net/http"
	"os"
	"path/filepath"

	// "strconv"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

func GetDetail() string {
	return "10"
}
func getDiscountConnection(host string) (*grpc.ClientConn, error) {
	wd, _ := os.Getwd()
	parentDir := filepath.Dir(wd)
	certFile := filepath.Join(parentDir+"/SQS", "keys", "server.crt")
	creds, _ := credentials.NewClientTLSFromFile(certFile, "")
	cn, _ := grpc.Dial(host, grpc.WithTransportCredentials(creds))
	fmt.Sprintf("%v", cn)
	return grpc.Dial(host, grpc.WithInsecure())
}

func main() {
	pb.Bar()
	log.Println("helllo")
	host := os.Getenv("DISCOUNT_SERVICE_HOST")
	if len(host) == 0 {
		host = "localhost:46001"
	}
	conn, err := getDiscountConnection(host)
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	//	fmt.

	defer conn.Close()
	cl := pb.NewSearchServiceClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*100)
	defer cancel()
	bar := []string{"hello"}
	req := &pb.FooRequest{Foo: 12, Bar: bar}
	res, err := cl.Search(ctx, req)
	tofro, err := cl.ToFro(ctx)
	err = tofro.Send(req)
	res, err = tofro.CloseAndRecv()
	fmt.Sprintf("%v %v", res, err)
	//c := pb.(conn)
}
