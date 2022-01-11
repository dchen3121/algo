# QUESTION:
# File downloader

# We are writing a downloader for very large files.
# The download works similarly to torrents, in the sense that the file chunks are received out of order.
# Chunks can come in any order, can start and end at any byte, can overlap, and can be duplicated.
# Write a download function which accepts the total number of bytes, byte ranges (inclusive), and a flag (for the bonus).

# Part 1:
# Return an integer percentage for how much of the file has been downloaded (i.e. 50 when half downloaded, 100 when all downloaded)

# Part 2 (Bonus):
# Let's say we want to check download data, but we aren't able to user checksums for some weird reason.
# Instead, we need to make sure every byte is downloaded twice.
# Change the download function so that if requires_duplicate flag is set to true, return either 0 for incomplete, or 100 when every byte is downloaded twice or more.

def download(num_bytes, byte_ranges, requires_duplicate):
    if not num_bytes:
        return 100
    if not byte_ranges:
        return 0
    # greedy approach
    # byte_ranges.sort(key=lambda byte_range: byte_range[0])
    if requires_duplicate:
        # greedily keep track of:
        # - last byte that was downloaded once
        # - last byte that was downloaded 2+ times
        last_byte_downloaded_once = -1
        last_byte_downloaded_twice_or_more = -1

        for start_byte, end_byte in byte_ranges:
            if start_byte > last_byte_downloaded_twice_or_more + 1:
                return 0
            last_byte_downloaded_twice_or_more = max(
                last_byte_downloaded_twice_or_more,
                min(last_byte_downloaded_once, end_byte)
            )
            last_byte_downloaded_once = max(end_byte, last_byte_downloaded_once)
        return 100 if last_byte_downloaded_twice_or_more == num_bytes - 1 else 0
    else:
        last_checked_byte = -1
        num_bytes_missed = 0

        for start_byte, end_byte in byte_ranges:
            if start_byte > last_checked_byte:
                num_bytes_missed += start_byte - last_checked_byte - 1
            last_checked_byte = max(end_byte, last_checked_byte)

        num_bytes_missed += num_bytes - last_checked_byte - 1
        return (num_bytes - num_bytes_missed) * 100 // num_bytes


print(download(5, [[3, 4]], False))
# 40
print(download(5, [[3, 4], [0, 2]], False))
# 100
print(download(5, [[0, 3], [0, 2], [0, 1], [1, 2], [1, 3], [1, 2], [1, 4]], True))
# 0
print(download(5, [[0, 4], [0, 1], [3, 4]], True))
# 0
print(download(5, [[0, 4], [0, 1], [2, 2], [3, 4]], True))
# 100
print(download(10, [[0, 6], [0, 4], [4, 9]], True))
# 0
print(download(10, [[0, 6], [0, 4], [4, 9], [7, 9]], True))
# 100
print(download(0, [], False))
# 100
print(download(10, [], False))
# 0