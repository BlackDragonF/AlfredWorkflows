//
//  main.m
//  gif2clipboard
//
//  Created by 码龙黑曜 on 2018/4/22.
//  Copyright © 2018年 码龙黑曜. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <AppKit/AppKit.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // check argument number
        if (argc != 2) {
            NSLog(@"Usage: gif2clipboard gif file");
            return -1;
        }
        
        // generate image absuluteURL/Data/Bitmap Representation
        NSString * imagePath = [NSString stringWithUTF8String:argv[1]];
        NSURL * imageURL = [[NSURL fileURLWithPath:imagePath] absoluteURL];
        NSData * imageData = [NSData dataWithContentsOfURL:imageURL];
        NSBitmapImageRep * imageRep = [NSBitmapImageRep imageRepWithData:imageData];

        // get general pasteboard, clear contents
        NSPasteboard * pasteBoard = [NSPasteboard generalPasteboard];
        [pasteBoard clearContents];
        // write possible types to pasteboard - macQQ uses furl / maipo uses GIF representation
        [pasteBoard setData:[imageURL dataRepresentation] forType:(__bridge NSString *)kUTTypeFileURL];
        [pasteBoard setData:[imageRep representationUsingType:NSBitmapImageFileTypeGIF properties:@{}] forType:(__bridge NSString *)kUTTypeGIF];
    }
    return 0;
}
