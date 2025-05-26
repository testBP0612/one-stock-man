<template>
	<section class="overflow-hidden bg-gray-50 py-16">
		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<svg
				class="text-primary-200 absolute top-full right-full translate-x-1/3 -translate-y-1/4 transform opacity-20 lg:translate-x-1/2 xl:-translate-y-1/2"
				width="404"
				height="404"
				fill="none"
				viewBox="0 0 404 404"
				role="img"
				aria-labelledby="svg-testimonial"
			>
				<title id="svg-testimonial">Testimonial background pattern</title>
				<defs>
					<pattern
						id="ad119f34-7694-4c31-947f-5c9d249b21f3"
						x="0"
						y="0"
						width="20"
						height="20"
						patternUnits="userSpaceOnUse"
					>
						<rect
							x="0"
							y="0"
							width="4"
							height="4"
							fill="currentColor"
						/>
					</pattern>
				</defs>
				<rect
					width="404"
					height="404"
					fill="url(#ad119f34-7694-4c31-947f-5c9d249b21f3)"
				/>
			</svg>

			<div class="relative">
				<h2
					class="text-center text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl"
				>
					收藏家的真實見證
				</h2>
				<p class="mx-auto mt-4 max-w-3xl text-center text-lg text-gray-500">
					聽聽我們平台上的收藏家如何尋找並收藏他們喜愛的台灣企業股票紀念品
				</p>
			</div>

			<div class="mt-12">
				<div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
					<div
						v-for="testimonial in testimonials"
						:key="testimonial.id"
						class="transform rounded-xl bg-white p-6 shadow-sm transition duration-500 hover:-translate-y-1 hover:shadow-md"
					>
						<div class="mb-4 flex items-center">
							<div class="h-12 w-12 flex-shrink-0">
								<img
									class="h-12 w-12 rounded-full"
									:src="testimonial.imageUrl"
									alt=""
								/>
							</div>
							<div class="ml-4">
								<h4 class="text-lg font-bold text-gray-900">{{ testimonial.name }}</h4>
								<p class="text-sm text-gray-500">{{ testimonial.title }}</p>
							</div>
						</div>
						<div class="mb-4 flex items-center">
							<template
								v-for="i in 5"
								:key="i"
							>
								<svg
									class="h-5 w-5"
									:class="i <= testimonial.rating ? 'text-accent-500' : 'text-gray-300'"
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 20 20"
									fill="currentColor"
								>
									<path
										d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
									/>
								</svg>
							</template>
						</div>
						<blockquote class="text-gray-700">
							<p>{{ testimonial.quote }}</p>
						</blockquote>
						<div class="mt-4 text-right text-sm">
							<span class="text-primary-600 font-medium">{{ testimonial.collectibles }}</span>
							件收藏
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup>
	// Sample testimonial data
	const testimonials = [
		{
			id: 1,
			name: '陳小明',
			title: '科技產業專業收藏家',
			rating: 5,
			quote:
				'這個平台幫助我找到許多台積電和聯發科的限量紀念品，特別是台積電40週年的金幣系列真的非常精美，是我收藏中最珍貴的物品之一。',
			imageUrl:
				'https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			collectibles: 42,
		},
		{
			id: 2,
			name: '林詩涵',
			title: '文創紀念品愛好者',
			rating: 4,
			quote:
				'透過這個平台，我發現很多企業的紀念品都融入了台灣文化元素，像是華碩的限定筆電和宏碁的文創周邊，都展現出科技與藝術的完美結合。',
			imageUrl:
				'https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			collectibles: 28,
		},
		{
			id: 3,
			name: '王大偉',
			title: '金融紀念品專家',
			rating: 5,
			quote:
				'身為一名金融業從業人員，我特別喜歡收集台灣金融機構的紀念品。這個平台幫助我找到許多中信金、富邦和國泰世華的限量紀念幣和模型。',
			imageUrl:
				'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
			collectibles: 65,
		},
	];
</script>
