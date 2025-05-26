<template>
	<div class="relative overflow-hidden bg-white">
		<div class="mx-auto max-w-7xl">
			<div
				class="relative z-10 bg-white pb-8 sm:pb-16 md:pb-20 lg:w-full lg:max-w-2xl lg:pb-28 xl:pb-32"
			>
				<svg
					class="absolute inset-y-0 right-0 hidden h-full w-48 translate-x-1/2 transform text-white lg:block"
					fill="currentColor"
					viewBox="0 0 100 100"
					preserveAspectRatio="none"
					aria-hidden="true"
				>
					<polygon points="50,0 100,0 50,100 0,100" />
				</svg>

				<main
					class="mx-auto mt-10 max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28"
				>
					<div class="sm:text-center lg:text-left">
						<h1
							class="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl md:text-6xl"
						>
							<span class="block xl:inline">探索台灣企業</span>
							<span class="text-primary-600 block xl:inline">精美股票紀念品</span>
						</h1>
						<p
							class="mt-3 text-base text-gray-500 sm:mx-auto sm:mt-5 sm:max-w-xl sm:text-lg md:mt-5 md:text-xl lg:mx-0"
						>
							收藏這些獨特的企業文化象徵，連結您與最喜愛的台灣企業，見證台灣經濟發展的獨特記憶。
						</p>
						<div class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start">
							<div class="rounded-md">
								<NuxtLink
									to="/companies"
									class="btn-primary w-full px-8 py-3 text-base font-medium"
								>
									探索公司
								</NuxtLink>
							</div>
						</div>
					</div>
				</main>
			</div>
		</div>
		<div class="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
			<img
				class="h-56 w-full object-cover sm:h-72 md:h-96 lg:h-full lg:w-full"
				src="https://images.pexels.com/photos/9532725/pexels-photo-9532725.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
				alt="股票紀念品展示"
			/>
		</div>
	</div>
</template>
