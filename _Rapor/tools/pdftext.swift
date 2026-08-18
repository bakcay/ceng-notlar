import Foundation
import PDFKit

let args = CommandLine.arguments
guard args.count > 1, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("PDF acilamadi\n".data(using: .utf8)!)
    exit(1)
}
var out = ""
for i in 0..<doc.pageCount {
    if let page = doc.page(at: i), let s = page.string { out += s + "\n" }
}
FileHandle.standardOutput.write(out.data(using: .utf8)!)
