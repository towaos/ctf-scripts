package main

import (
	"encoding/base64"
	"fmt"
)

func main() {
	encodedStrings := []string{
		"bnRfdGg0dA==",
		"fQ==",
		"+TH2Ria",
		"ZTFmZjA2Mw==",
		"KiZP+uA=",
		"mUKl4q4=",
		"BbzQg10=",
		"XzM0c3lfdA==",
		"ezF0X3c0cw==",
		"Qj9atMY=",
		"cGljb0NURg==",
		"UJddNj4=",
		"u1n7aWg=",
		"okKTBr8=",
		"ZDQkP3U=",
		"UBcZPyY=",
		"y88/pdA=",
		"MwbMYqQ=",
		"+RV8NVY=",
		"YmhfNHJfMg==",
		"lwFp5w0=",
	}

	for _, encoded := range encodedStrings {
		decoded, err := base64.StdEncoding.DecodeString(encoded)
		if err != nil {
			fmt.Printf("Error decoding %s: %v\n", encoded, err)
		} else {
			fmt.Printf("Decoded (%s): %s\n", encoded, string(decoded))
		}
	}
}
