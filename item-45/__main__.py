from datetime import datetime, timedelta
from functools import wraps
from itertools import repeat


def _print_fn(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        fn_name = fn.__name__.replace("_", " ")
        indent = 2
        div = "".join(repeat("=", len(fn_name) + indent * 2))
        title = "\n".join([div, f"{''.join(repeat(' ', indent))}{fn_name}", div])
        print(title)
        fn(*args, **kwargs)
        print("\n")

    return wrapper


@_print_fn
def _use_property_to_patch_poorly_implemented_classes():
    class Bucket:
        def __init__(self, period: int, /):
            self.period_delta = timedelta(seconds=period)
            self.reset_time = datetime.now()
            self.quota = 0

        def __repr__(self):
            return f"Bucket(quota={self.quota})"

    def fill(bucket: Bucket, amount: int, /):
        """fill.

        fill a bucket with an amount

        if the time since the reset time is greater than the period this bucket
        is eligible to have a quota, then reset the quota

        :param bucket:
        :type bucket: Bucket
        :param amount:
        :type amount: int
        """
        now = datetime.now()

        if (now - bucket.reset_time) > bucket.period_delta:
            bucket.quota = 0
            bucket.reset_time = now

        bucket.quota += amount

    def deduct(bucket: Bucket, amount: int, /):
        now = datetime.now()

        if (now - bucket.reset_time) > bucket.period_delta:
            return False

        if amount > bucket.quota:
            return False

        bucket.quota -= amount

        return True

    bucket = Bucket(1)
    print(f"after instantiation: {bucket}")

    fill(bucket, 100)
    print(f"after fill 100: {bucket}")

    deduct(bucket, 99)
    print(f"after deduct 99: {bucket}")

    deduct(bucket, 3)
    print(f"after deduct 3: {bucket}")
    print(
        "\nat this point we don't know why we can't deduct anymore because the"
        "Bucket implementation doesn't indicate what quota we started with."
        "To fix this, we can use @property and subclassing to create an improved"
        "Bucket class that retains the same interface as Bucket\n"
    )

    class PatchedBucket(Bucket):
        def __init__(self, period: int = 1, /):
            self.max_quota = 0
            self.quota_consumed = 0
            super().__init__(period)

        def __repr__(self):
            attributes = [
                f"\t{attr}={getattr(self, attr)}"
                for attr in ["quota", "quota_consumed"]
            ]
            xs = ["PatchedBucket(", *attributes, ")"]
            string = "\n".join(xs)

            return string

        @property
        def quota(self):
            return self.max_quota - self.quota_consumed

        @quota.setter
        def quota(self, amount: int, /):
            delta = self.max_quota - amount

            if amount == 0:
                self.quota_consumed = 0
                self.max_quota = 0

            elif delta < 0:
                assert self.quota_consumed == 0
                self.max_quota = amount

            else:
                assert self.max_quota >= self.quota_consumed
                self.quota_consumed += delta

    bucket = PatchedBucket(1)
    print(f"after instantiation:\n{bucket}\n")

    fill(bucket, 100)
    print(f"after fill 100:\n{bucket}\n")

    deduct(bucket, 99)
    print(f"after deduct 99:\n{bucket}\n")

    deduct(bucket, 3)
    print(f"after deduct 3:\n{bucket}\n")


if __name__ == "__main__":
    _use_property_to_patch_poorly_implemented_classes()
