	Goal of the task 
An agent undercover sends secret messages to the headquarters. In order to make eavesdropping the whole content of her message harder, she divides the original message into smaller parts and sends each part through different public communication channel such as e-mail, text message and social media. As a further security measure, before sending she encodes each message part in a way that the content of any segment of the secret message can be revealed by an eavesdropper only if they manage to obtain all message parts.

Our task at the headquarters is to decode and assemble the original message from the encoded message parts received through the public communications channels.

Encoding process:
In order to test the communication, the agent wants to send the message ‘Hello!’ through two different public channels, e.g., e-mail and Twitter. Therefore, she divides the message into hs = 2 parts (number of different public communication channels available), each containing ms = 3 original characters (ms = #characters in message / hs) given by their ASCII representation, i.e., 72 101 108 and 108 111 33, respectively. In order to keep track of the content of each encoded message part during the encryption process, an encoding header with length hs is attached in front of the encoded characters. The above representation of the original message parts before the encoding process look like as follows, given in the format of [encoding header] [encoded characters].
Part 1: [1 0] [72 101 108]
Part 2: [0 1] [108 111 33]

During the encoding the agent linearly combines the message parts with each other where she makes sure that the hsxhs quadratic matrix formed by the encoding headers has full rank (i.e., the operators at the headquarters will be able to decode the message if they have access to all message parts), and also all ASCII values in both the encoding header and in the encoded characters are between 33 and 126 to get printable ASCII characters which can be used during the communication. Two encoded message parts which satisfy the above requirements are:
Part 1: [122 122] [116 83 57]
Part 2: [113 74] [126 69 41]

Note that, the jth number in the encoding header represents how many times the jth original massage part was added to that particular encoded message part, while the ith encoded character is the sum of the ASCII values of the ith characters in the original message parts modulo 127. For example, the 2nd character 69 in the second message is the the results of (113*101 + 74*111) mod 127 = 69.

The secret messages consist of the five characters corresponding to the ASCII values in the encoded message parts, namely:
Sent in e-mail: zztS9
Tweeted in a post: qJ~E)

Decoding example:
At the headquarters two messages zztS9 and qJ~E) were detected through e-mail and Twitter, respectively. Therefore, the operators know that hs = 2 and ms = 5 - 2 = 3, which gives the following representation:
[122 122] [116 83 57]
[113 74] [126 69 41]

The operators at the headquarters have to follow the reverse process of encoding - i.e., using modulo arithmetic (modulo addition and multiplication) over finite field with characteristic of 127 - to obtain an identity matrix on the hsxhs encoding header part, while the same operations are performed on the encoded characters as well:
[1 0] [72 101 108]
[0 1] [108 111 33]

As a result, each encoded message part contains only a single original message part, which after appending the ASCII characters 72 101 108 and 108 111 33 reveals the original secret message ‘Hello!’ sent by the agent.
Input
Line 1: An integer hs for the size of the encoding header.
Line 2: An integer ms for the size of the encoded characters in each encoded message part.
Next hs lines: A string containing hs + ms characters.
Output
A single line containing the decoded string.
Constraints
1 ≤ hs ≤ 10
1 ≤ ms ≤ 40
The input strings contain printable ASCII characters (from the range of 32 < ASCII and ASCII < 127).